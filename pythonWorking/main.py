
#cd "C:\Users\jaese\Desktop\programming folder\python\pythonWorking"

import sys
import re
from datetime import date
from storage import loadEntries
import commands


def usage():
    print("""사용법:
    python main.py add/new/create
    python main.py list
    python main.py today
    python main.py date YYYY-MM-DD\n\n""")


def commandCheck(argv):
    if len(argv) <= 1:
        print("\n\n명령어를 입력하세요.")
        usage()
        return 
    return True


def dateCheck(command, argv):
    if len(argv) <= 2 :
        print(f"""\n\n잘못된 사용법입니다.
예: python main.py {command} YYYY-MM-DD\n\n""")
        return 
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", argv[2]):
        print(f"""\n\n날짜는 YYYY-MM-DD 형식으로 입력하세요.
사용법:
  python working.py {command} YYYY-MM-DD\n\n""")
        return 
    return argv[2]


def searchCheck(argv):
    if len(argv) <= 2:
        print("""\n\n검색어를 입력하세요.
사용법:
  python main.py search <keyword>\n\n""")
        return 
    return argv[2]


def main():
    if not commandCheck(sys.argv):
        return
    command = sys.argv[1]
    command = command.lower()
    
    match command:
        
        case "add" | "new" | "create":
            commands.addEntry(str(date.today()))

        case "list":
            commands.showAll(loadEntries())

        case "today":
            commands.showByDate(loadEntries(), str(date.today()))

        case "update":
            dc = dateCheck(command, sys.argv)
            if dc:
                commands.update(loadEntries(), dc)

        case "delete":
            dc= dateCheck(command, sys.argv)
            if dc:
                commands.delete(loadEntries(), dc)
            
        case "date":
            dc = dateCheck(command, sys.argv)
            if dc:
                commands.showByDate(loadEntries(), dc)

        case "search":
            sc = searchCheck(sys.argv)
            if sc:
                commands.search(loadEntries(), sc)

        case "stats":
            commands.stats(loadEntries())

        case "export":
            commands.export(loadEntries())

        case _:
            print("\n\n지원하지 않는 명령어 입니다.")
            usage()


if __name__ == "__main__":
    main()

