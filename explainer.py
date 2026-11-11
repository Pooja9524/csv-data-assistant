from groq_client import chat
from profiler import profile

# Instructions for the model
SYSTEM = """You are a data analyst. You are given exact statistics about a CSV file.
Explain the dataset in plain English in 5 to 8 short sentences.
Use only the numbers given. Do not invent any numbers.
Do not mention columns whose name ends in 'id'.
The 'most common' list shows only the top values, not all of them.
Use 'distinct values' to say how many different values a column has.
Mention any missing values."""


def build_summary(row_count, stats):
    # Turn the statistics into plain text the model can read
    lines = ["Rows: " + str(row_count)]
    for col, s in stats.items():
        if s["count"] > 0 and not s["text"]:
            avg = s["total"] / s["count"]
            lines.append(f"{col}: number, missing {s['missing']}, average {avg:.2f}, min {s['min']}, max {s['max']}")
        else:
            top = ", ".join(f"{v} ({n})" for v, n in s["text"].most_common(3))
            lines.append(f"{col}: text, missing {s['missing']}, distinct values {len(s['text'])}, most common: {top}")
    return "\n".join(lines)


def explain(path):
    # 1. Python reads every row and calculates the facts
    row_count, stats = profile(path)

    # 2. Turn the facts into text
    summary = build_summary(row_count, stats)

    # 3. The model explains the facts in plain English
    return chat(SYSTEM, summary)