"""Write the negative-control records for quit_paused_v1/v2 from one passing candidate record (D9 offline validation).
Usage: make_quit_negatives.py SOURCE_RESULT_JSON OUT_DIR   (OUT_DIR must not exist; the source is only read)"""
import json
from pathlib import Path
import sys

r = json.load(open(sys.argv[1])); out = Path(sys.argv[2]); out.mkdir(parents=True)
cases = {
    "N1-pause-false": lambda x: x["details"]["d"].__setitem__("paused_before_quit", False),
    "N2-pause-absent": lambda x: x["details"]["d"].pop("paused_before_quit"),
    "N3-pause-string": lambda x: x["details"]["d"].__setitem__("paused_before_quit", "true"),
    "N4-oldd-false": lambda x: x["checks"].__setitem__("d", False),
    "N5-invalid-set": lambda x: x.__setitem__("invalid", "oracle error: injected"),
    "N6-details-d-null": lambda x: x["details"].__setitem__("d", None),
    "N7-oldd-string": lambda x: x["checks"].__setitem__("d", "true"),
}
for name, fn in cases.items():
    x = json.loads(json.dumps(r)); fn(x); (out / f"{name}.json").write_text(json.dumps(x, indent=1))
(out / "N8-not-json.json").write_text("{not json")
print("written", len(cases) + 1)
