import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "federer_companies_pune.csv"

CRITERIA = [
    "c3_differentiation",
    "c4_decision_maker",
    "c5_growing_sector",
    "c6_growth_signals",
    "c7_systems_maturity",
    "c8_leadership_succession",
]


def band(score: float) -> str:
    if score >= 80:
        return "A - Strong Federer"
    if score >= 60:
        return "B - Probable Federer"
    if score >= 40:
        return "C - Borderline"
    return "D - Not ICP"


def main() -> None:
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    errors = []
    for i, row in enumerate(rows, start=2):
        score = sum(float(row[c]) for c in CRITERIA)
        stated = float(row["federer_score"])
        if abs(score - stated) > 0.01:
            errors.append(f"Line {i}: score mismatch {score} vs {stated}")
        if row["band"] != band(score):
            errors.append(f"Line {i}: band mismatch {row['band']} vs {band(score)}")
        if row["c7_systems_maturity"] in {"", "0", "0.0"}:
            errors.append(f"Line {i}: C7 is zero/blank, automatic fail")
        if row["e1_producer"].upper().startswith("FAIL") or row["e2_accessible"].upper().startswith("FAIL"):
            errors.append(f"Line {i}: eligibility gate failed")

    result = {
        "rows": len(rows),
        "errors": errors,
        "band_counts": {
            "A": sum(1 for r in rows if r["band"].startswith("A")),
            "B": sum(1 for r in rows if r["band"].startswith("B")),
            "C": sum(1 for r in rows if r["band"].startswith("C")),
            "D": sum(1 for r in rows if r["band"].startswith("D")),
        },
    }
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
