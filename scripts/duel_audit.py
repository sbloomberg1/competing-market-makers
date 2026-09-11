"""Reference fields, seat rotations, identical entries, and stress scenarios."""
from dataclasses import asdict
import json
from pathlib import Path
from experiment import Local, evaluate

rows = []
field = ["adaptive", "wide", "tight", "static"]
for seed in range(5):
    for rotation in range(4):
        names = field[rotation:] + field[:rotation]
        result = evaluate(seed, [Local(n) for n in names], {"episodes": 8192}, mode="duel")
        rows.append({"case": "seat_rotation", "sample": seed, "policies": names,
                     "rotation": rotation, **asdict(result)})
    for case, names, stress in [("identical", ["adaptive"] * 4, False),
                                ("losing_field", ["static"] * 4, False),
                                ("stress", field, True)]:
        result = evaluate(seed, [Local(n) for n in names], {"episodes": 8192}, mode="duel", stress=stress)
        rows.append({"case": case, "sample": seed, "policies": names, **asdict(result)})
    Path("evidence/duel-audit.json").write_text(json.dumps(rows, indent=2) + "\n")
    print("completed sample", seed, flush=True)
