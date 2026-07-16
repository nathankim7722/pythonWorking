
import json

LOG_FILE = "pythonWorking.md"


def loadEntries():
    entries = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return entries

    rawEntries = content.strip().split("\n\n\n")
    for raw in rawEntries:
        raw = raw.strip()
        if not raw:
            continue
        first_line = raw.split("\n")[0]
        date_str = first_line.replace("*", "").strip()
        entries.append({"date": date_str, "text": raw})
    return entries


def saveEntries(entries):
 with open(LOG_FILE, "w", encoding="utf-8") as file:
    if entries:
        file.write("\n\n\n".join(e["text"] for e in entries) + "\n\n\n")
    else:
        file.write("")


def appendEntries(entries):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entries)


EXPORT_FILE = "pythonWorking.json"

def saveJson(data):
    with open(EXPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)




