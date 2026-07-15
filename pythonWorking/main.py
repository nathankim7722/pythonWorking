
import sys
import re
from datetime import date
 
from storage import loadEntries
import commands



def main():

    command = sys.argv[1]

    if command == "list":
        commands.showAll(loadEntries())

    elif command == "today":
        commands.showByDate(loadEntries(), str(date.today()))

    elif command =="update":
        commands.update(loadEntries(), sys.argv[2])

    elif command == "delete":
        commands.delete(loadEntries(), sys.argv[2])

    elif command == "date":
        commands.showByDate(loadEntries(), sys.argv[2])
    
    elif command == "search":
        commands.search(loadEntries(), sys.argv[2])
    
    elif command == "stats":
        commands.stats(loadEntries())

    elif command == "mostUsed":
        commands.mostUsed(loadEntries())

    else:
        commands.addEntry(str(date.today()))


if __name__ == "__main__":
    main()

