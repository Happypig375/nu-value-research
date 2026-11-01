"""Pure declared configuration/history/lifecycle checks; no engine or process calls."""
import json
import math
import re
from collections import Counter

SCENE = 'Game/Gameplay/Scene'
SOURCE = SCENE + '/Villa/Palm'
LOCAL = SCENE + '/Villa-0002/Palm-0009'
HISTORY = 'PropagatedDescriptorOpt'
LINK = 'PropagationSourceOpt'
TRANSFORMS = {'Position', 'PositionLocal', 'Rotation', 'RotationLocal', 'Scale', 'ScaleLocal'}
SELECTED = TRANSFORMS | {'Size', 'Offset', 'MountOpt', 'Static', 'Clipped', 'BodyShape',
                         'StaticModel', 'MaterialProperties', LINK, HISTORY}
MATERIAL = ('AlbedoOpt', 'RoughnessOpt', 'MetallicOpt', 'AmbientOcclusionOpt', 'EmissionOpt',
            'HeightOpt', 'IgnoreLightMapsOpt', 'OpaqueDistanceOpt', 'FinenessOffsetOpt',
            'ScatterTypeOpt', 'SpecularScalarOpt', 'SubsurfaceCutoffOpt', 'SubsurfaceCutoffMarginOpt',
            'RefractiveIndexOpt', 'ClearCoatOpt', 'ClearCoatRoughnessOpt')
TINT = ['Some', ['0.25', '0.5', '0.75', '1']]


def symbol(text):
    tokens = re.findall(r'"(?:\\.|[^"\\])*"|\[|\]|[^\s\[\]"]+', text)
    position = 0

    def parse():
        nonlocal position
        if position >= len(tokens):
            raise ValueError('Unexpected end of symbol.')
        token = tokens[position]
        position += 1
        if token == '[':
            values = []
            while position < len(tokens) and tokens[position] != ']':
                values.append(parse())
            if position >= len(tokens):
                raise ValueError('Unclosed symbol.')
            position += 1
            return values
        if token == ']':
            raise ValueError('Unexpected bracket.')
        return json.loads(token) if token.startswith('"') else token

    result = parse()
    if position != len(tokens):
        raise ValueError('Trailing symbol input.')
    return result


def pairs(rows):
    if not isinstance(rows, list) or any(not isinstance(r, list) or len(r) != 2 for r in rows):
        raise ValueError('Expected named field pairs.')
    result = dict(rows)
    if len(result) != len(rows):
        raise ValueError('Duplicate named field.')
    return result


def equal(a, b, transform=False):
    if not transform:
        return a == b
    if isinstance(a, list) or isinstance(b, list):
        return (isinstance(a, list) and isinstance(b, list) and len(a) == len(b)
                and all(equal(x, y, True) for x, y in zip(a, b)))
    try:
        x, y = float(a), float(b)
    except (TypeError, ValueError):
        return False
    return math.isfinite(x) and math.isfinite(y) and abs(x - y) <= 0.0001


def tree(group):
    if not isinstance(group, list) or len(group) != 3 or group[0] != 'GroupDispatcher':
        raise ValueError('Wrong group descriptor.')
    nodes = {}

    def walk(parent, children):
        for row in children:
            if not isinstance(row, list) or len(row) != 3:
                raise ValueError('Wrong entity descriptor.')
            props = pairs(row[1])
            name = props['Name']
            address = parent + '/' + name
            if address in nodes:
                raise ValueError('Duplicate descriptor address.')
            nodes[address] = {'Address': address, 'Parent': parent, 'Name': name,
                              'Dispatcher': row[0], 'Properties': props,
                              'Children': [pairs(child[1])['Name'] for child in row[2]], 'Raw': row}
            walk(address, row[2])

    walk(SCENE, group[2])
    return nodes


def fixed_originals(group):
    original = tree(group)
    palms = {a for a, n in original.items() if n['Properties'].get('StaticModel') == ['Gameplay', 'PalmTree']}
    declared = {SCENE + '/' + v + '/' + p
                for v in ('Villa', 'Villa-0002', 'Villa-0003', 'Villa-0004')
                for p in ('Palm', 'Palm-0009', 'Palm-0010', 'Palm-0011', 'Palm-0012', 'Palm-0013', 'Palm-0014', 'Palm-0016')}
    links = {a: n['Properties'][LINK] for a, n in original.items() if LINK in n['Properties']}
    histories = {a for a, n in original.items() if HISTORY in n['Properties']}
    if (len(original), len(group[2]), len(links), len(histories)) != (197, 19, 166, 11) or palms != declared:
        raise ValueError('Wrong fixed original scene/family.')
    if any(links.get(a) != ['Some', SOURCE] for a in palms - {SOURCE}) or SOURCE in links:
        raise ValueError('Wrong original direct palm links.')
    return original, palms


def nodes(capture):
    result = {r['Address']: r for r in capture['Entities']}
    if len(result) != len(capture['Entities']):
        raise ValueError('Duplicate observation address.')
    return result


def properties(row):
    result = {p['Name']: p for p in row['Properties']}
    if len(result) != len(row['Properties']):
        raise ValueError('Duplicate observation property.')
    return result


def material(value):
    result = pairs(value)
    if set(result) != set(MATERIAL):
        raise ValueError('Material must retain all 16 named current fields.')
    return result


class Findings:
    def __init__(self):
        self.rows = []

    def flag(self, kind, phase, name, expected=None, actual=None):
        self.rows.append(dict(kind=kind, phase=phase, name=name, expected=expected, actual=actual))

    def check(self, passed, kind, phase, name, expected=None, actual=None):
        if not passed:
            self.flag(kind, phase, name, expected, actual)


def check_capture(data, original, f, phase):
    current = nodes(data)
    mode = [data[k] for k in ('Imperative', 'Accompanied', 'Advancing', 'Halted', 'GameState', 'GameplaySelected', 'UpdateTime')]
    f.check(mode == [False, True, False, True, 'Gameplay', True, '0'], 'invalid', phase, 'mode_clock_selection', actual=mode)
    f.check('SDL_WINDOW_HIDDEN' in data['WindowFlags'], 'invalid', phase, 'hidden_window')
    for address, row in current.items():
        f.check(row['Original'] == (address in original), 'invalid', phase, address + ':original_tag')
        if address not in original:
            continue
        expected = original[address]
        props = properties(row)
        wanted = set(expected['Properties']) | SELECTED
        f.check(set(props) == wanted, 'invalid', phase, address + ':observation_property_roster', sorted(wanted), sorted(props))
        for name, prop in props.items():
            f.check(not prop['Error'], 'invalid', phase, address + ':' + name + ':conversion', actual=prop['Error'])
            f.check(prop['ExpectedPresent'] == (name in expected['Properties']), 'invalid', phase, address + ':' + name + ':original_presence')
            if name in expected['Properties']:
                f.check(symbol(prop['ExpectedSymbol']) == expected['Properties'][name], 'invalid', phase, address + ':' + name + ':original_symbol')
    return current


def compare_nodes(before, after, original, f, phase, kind='adverse', palm_albedo=None,
                  local_roughness=None, advancing_histories=(), keep_ids=False):
    """Preserve every declared property; only explicitly supplied field exceptions apply."""
    for address in original:
        old, new = before.get(address), after.get(address)
        if old is None or new is None:
            f.flag(kind, phase, address + ':exists', True, new is not None)
            continue
        for key in ('Name', 'Parent', 'Dispatcher', 'Persistent', 'Protection'):
            f.check(old[key] == new[key], kind, phase, address + ':' + key, old[key], new[key])
        if keep_ids:
            f.check(old['Id'] == new['Id'], kind, phase, address + ':preparation_identity', old['Id'], new['Id'])
        wanted_children = sorted(original[address]['Children'])
        actual_children = sorted(n for n in new['Children'] if address + '/' + n in original)
        f.check(actual_children == wanted_children, kind, phase, address + ':original_children', wanted_children, actual_children)
        pold, pnew = properties(old), properties(new)
        for name in set(original[address]['Properties']) | SELECTED:
            a, b = pold.get(name), pnew.get(name)
            if a is None or b is None or a['Error'] or b['Error']:
                continue  # check_capture assigns observer invalidity, not a silent configuration pass.
            if name == HISTORY and address in advancing_histories:
                continue  # The separate exact current-source correspondence check owns these.
            if name == 'MaterialProperties' and (palm_albedo is not None and address in palm_albedo or address == local_roughness):
                if not (a['Found'] and b['Found']):
                    f.flag(kind, phase, address + ':material_presence', True, b['Found'])
                    continue
                try:
                    desired = material(symbol(a['Value']))
                    actual = material(symbol(b['Value']))
                except ValueError as error:
                    f.flag(kind, phase, address + ':material_layout', actual=str(error))
                    continue
                if palm_albedo is not None and address in palm_albedo:
                    desired['AlbedoOpt'] = TINT
                if address == local_roughness:
                    desired['RoughnessOpt'] = ['Some', '0.75']
                for field in MATERIAL:
                    f.check(desired[field] == actual[field], kind, phase, address + ':material:' + field, desired[field], actual[field])
                continue
            same = a['Found'] == b['Found']
            if same and a['Found']:
                same = equal(symbol(a['Value']), symbol(b['Value']), name in TRANSFORMS)
            f.check(same, kind, phase, address + ':' + name, a, b)


def check_baseline(ready, original, palms, f, phase):
    f.check(set(ready) >= set(original), 'invalid', phase, 'all_originals_ready')
    for address, expected in original.items():
        row = ready.get(address)
        if row is None:
            continue
        for key in ('Name', 'Parent', 'Dispatcher'):
            f.check(row[key] == expected[key], 'invalid', phase, address + ':' + key)
        props = properties(row)
        for name in set(expected['Properties']) | {LINK, HISTORY}:
            p = props.get(name)
            wanted = expected['Properties'].get(name, 'None')
            f.check(p is not None and p['Found'] and not p['Error'] and
                    equal(symbol(p['Value']), wanted, name in TRANSFORMS), 'invalid', phase, address + ':' + name + ':original_value')
        if address in palms:
            p = props.get('MaterialProperties')
            f.check(p is not None and p['Found'] and material(symbol(p['Value'])) == dict.fromkeys(MATERIAL, 'None'),
                    'invalid', phase, address + ':all_none_material')


def check_links(current, original, f, phase, kind='adverse'):
    for address, expected in original.items():
        if address not in current:
            continue
        p = properties(current[address]).get(LINK)
        value = symbol(p['Value']) if p and p['Found'] and not p['Error'] else None
        wanted = expected['Properties'].get(LINK, 'None')
        f.check(value == wanted, kind, phase, address + ':source_link', wanted, value)
        if isinstance(value, list) and len(value) == 2 and value[0] == 'Some':
            f.check(value[1] in current, kind, phase, address + ':resolved_source', value[1], value[1] in current)


def check_history(current, originals, source_trees, operator, f, phase):
    for address, raw in source_trees.items():
        if operator != 'P':
            continue
        node = current.get(address)
        if node is None:
            f.flag('adverse', phase, address + ':history_source_missing')
            continue
        prop = properties(node).get(HISTORY)
        value = symbol(prop['Value']) if prop and prop['Found'] and not prop['Error'] else None
        wanted = [raw[0], [pair for pair in raw[1] if pair[0] != HISTORY], raw[2]]
        # Strip only the top-level self history. Nested history remains part of both trees.
        f.check(value == ['Some', wanted], 'adverse', phase, address + ':current_source_history_correspondence', ['Some', wanted], value)


def lifecycle(events, final_counter, captures, boundaries, original, operator, f, phase):
    start_findings = len(f.rows)
    ordinals = [e['Ordinal'] for e in events]
    f.check(isinstance(final_counter, int) and final_counter >= 0 and ordinals == list(range(1, final_counter + 1)),
            'lifecycle', phase, 'independent_callback_counter_and_contiguous_ordinals', final_counter, ordinals)
    for a, b in zip(boundaries, boundaries[1:]):
        f.check(a['Counter'] <= b['Counter'], 'invalid', phase, 'monotonic_phase_counters')
        for event in events:
            if a['Counter'] < event['Ordinal'] <= b['Counter']:
                f.check(event['Phase'] == a['Name'], 'lifecycle', phase, 'event_phase', a['Name'], event['Phase'])
    f.check(boundaries[-1]['Counter'] == final_counter, 'lifecycle', phase, 'counter_after_cleanup', final_counter, boundaries[-1]['Counter'])
    for event in events:
        f.check(not event['Error'], 'lifecycle', phase, 'callback_observation_error', actual=event['Error'])
        f.check(event['Kind'] in ('register', 'unregister', 'mount'), 'lifecycle', phase, 'known_recorded_kind', actual=event['Kind'])
    for capture in captures:
        identities = [row['Id'] for row in capture['Entities']]
        f.check(all(identities) and len(set(identities)) == len(identities), 'lifecycle', phase,
                capture['Label'] + ':nonempty_unique_live_ids', 'one nonempty ID per live address', identities)
    for before, after in zip(captures, captures[1:]):
        live = {a: row['Id'] for a, row in nodes(before).items()}
        owners = {identity: address for address, identity in live.items()}
        for event in events:
            if not before['Counter'] < event['Ordinal'] <= after['Counter'] or not event['Address'].startswith(SCENE + '/'):
                continue
            address, identity = event['Address'], event['Id']
            if event['Kind'] == 'register':
                f.check(address not in live and bool(identity) and identity not in owners and event['Entity'] and event['Exists'],
                        'lifecycle', phase, 'register_identity:' + address, 'new address and currently unused ID',
                        {'existing_address_id': live.get(address), 'existing_id_owner': owners.get(identity)})
                live[address] = identity
                if identity not in owners:
                    owners[identity] = address
            elif event['Kind'] == 'unregister':
                f.check(address in live and live[address] == identity and owners.get(identity) == address and event['Entity'] and event['Exists'],
                        'lifecycle', phase, 'unregister_identity:' + address, live.get(address), identity)
                live.pop(address, None)
                if owners.get(identity) == address:
                    owners.pop(identity)
        wanted = {a: row['Id'] for a, row in nodes(after).items()}
        f.check(live == wanted, 'lifecycle', phase, before['Label'] + '_to_' + after['Label'] + ':endpoint_conservation', wanted, live)
    counts = {kind: Counter(e['Address'] for e in events if e['Phase'] == 'operator' and e['Kind'] == kind)
              for kind in ('register', 'unregister')}
    predicted = {}
    for address in original:
        direct = original[address]['Properties'].get(LINK) == ['Some', SOURCE]
        ancestor = any(address == SCENE + '/' + v or address.startswith(SCENE + '/' + v + '/')
                       for v in ('Villa-0002', 'Villa-0003', 'Villa-0004'))
        predicted[address] = (int(direct) + int(ancestor)) if operator == 'P' else 0
    divergent = {address: {'predicted_pairs': n, 'register': counts['register'][address], 'unregister': counts['unregister'][address]}
                 for address, n in predicted.items() if counts['register'][address] != n or counts['unregister'][address] != n}
    valid = not any(row['kind'] == 'lifecycle' for row in f.rows[start_findings:])
    return {'measure_established': valid, 'prediction_divergence': divergent,
            'expected_original_occurrences': sum(predicted.values()),
            'observed_original_register': sum(n for a, n in counts['register'].items() if a in original),
            'observed_original_unregister': sum(n for a, n in counts['unregister'].items() if a in original),
            'all_operator_counts_by_address': {k: dict(v) for k, v in counts.items()},
            'delivery_limit': 'Callback integrity and endpoint conservation do not independently prove all internal actions emitted/delivered an event.'}
