
import sys
import re
from datetime import date
 
from storage import loadEntries
import commands



def main():
    if not commands.commandCheck(sys.argv):
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
            dateCheck = commands.dateCheck(command, sys.argv)
            if dateCheck:
                commands.update(loadEntries(), dateCheck)

        case "delete":
            dateCheck = commands.dateCheck(command, sys.argv)
            if dateCheck:
                commands.delete(loadEntries(), dateCheck)
            
        case "date":
            dateCheck = commands.dateCheck(command, sys.argv)
            if dateCheck:
                commands.showByDate(loadEntries(), dateCheck)

        case "search":
            searchCheck = commands.searchCheck(command, sys.argv)
            if searchCheck:
                commands.search(loadEntries(), sys.argv[2])

        case "stats":
            commands.stats(loadEntries())

        case "export":
            commands.export(loadEntries())

        case _:
            commands.usage()


if __name__ == "__main__":
    main()

