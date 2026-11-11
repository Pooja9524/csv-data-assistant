import csv
import sys
from collections import Counter


def is_number(text):
    # True if the text can be turned into a number, like "12" or "3.5"
    try:
        float(text)
        return True
    except ValueError:
        return False


def profile(path):
    stats = {}
    row_count = 0

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Prepare an empty set of counters for every column
        for col in reader.fieldnames:
            stats[col] = {
                "missing": 0,
                "count": 0,
                "total": 0.0,
                "min": None,
                "max": None,
                "text": Counter(),
            }

        # Read the file one row at a time, so any size works
        for row in reader:
            row_count += 1
            for col, value in row.items():
                s = stats[col]
                value = (value or "").strip()

                if value == "":
                    s["missing"] += 1
                elif is_number(value):
                    n = float(value)
                    s["count"] += 1
                    s["total"] += n
                    s["min"] = n if s["min"] is None else min(s["min"], n)
                    s["max"] = n if s["max"] is None else max(s["max"], n)
                else:
                    s["text"][value] += 1

    return row_count, stats


def show(row_count, stats):
    print("Rows:", row_count)
    for col, s in stats.items():
        if s["count"] > 0 and not s["text"]:
            avg = s["total"] / s["count"]
            print(f"{col}: number | missing {s['missing']} | avg {avg:.2f} | min {s['min']:.2f} | max {s['max']:.2f}")
        else:
            top = ", ".join(f"{v} ({n})" for v, n in s["text"].most_common(3))
            print(f"{col}: text | missing {s['missing']} | top: {top}")


if __name__ == "__main__":
    rows, stats = profile(sys.argv[1])
    show(rows, stats)