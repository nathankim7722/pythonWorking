

from config import LOG_FILE, EXPORT_FILE, DATE_FORMAT, JSON_INDENT, LINE_INDENT
import json


def load_entries():
    entries = []

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        return entries

    raw_entries = content.strip().split(LINE_INDENT)

    for raw in raw_entries:
        raw = raw.strip()

        if not raw:
            continue

        first_line = raw.split("\n")[0]
        date_str = first_line.replace("*", "").strip()
        entries.append({"date": date_str, "text": raw})

    return entries


def save_entries(entries):
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        if entries:
            file.write(
                LINE_INDENT.join(entry["text"] for entry in entries)
                + LINE_INDENT
            )
        else:
            file.write("")


def append_entries(entry):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry)


def save_json(data):
    with open(EXPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=JSON_INDENT)

