
import re
from datetime import date
 
from storage import loadEntries
import commands


def main():
    command = input("명령어를 입력하세요 (list / today / YYYY-MM-D / update: YYYY-MM-DD / delete: YYYY-MM-DD), 새 로그 작성은 Enter: ").strip()

    if command == "list" or command == "List":
        commands.showAll(loadEntries())
    elif command == "today" or command == "Today":
        commands.showByDate(loadEntries(), str(date.today()))
    elif re.match(r"^update:\s*\d{4}-\d{2}-\d{2}$",command):
        commands.update(loadEntries(), command)
    elif re.match(r"^delete:\s*\d{4}-\d{2}-\d{2}$",command):
        commands.delete(loadEntries(), command)
    elif re.match(r"^\d{4}-\d{2}-\d{2}$", command):
        commands.showByDate(loadEntries(), command)
    else:
        commands.addEntry(str(date.today()))


if __name__ == "__main__":
    main()

