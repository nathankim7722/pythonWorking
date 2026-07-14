
from storage import loadEntries, saveEntries, appendEntries

def log(dateStr):

    work = input("오늘 한 일은?: ") or "없음"
    learn = input("배운것은?: ") or "없음"

    if work == "없음" and learn == "없음":
        message = "오늘은 아무것도 안했네요. 내일은 더 열심히 해봐요!"
    elif work == "없음" or learn == "없음":
        message = "오늘은 일부분만 했네요. 내일은 더 열심히 해봐요!"
    else:
        message = "오늘 하루도 수고 많았어요!"

    return f"""**{dateStr}**

오늘 한 일은?
 - {work}

배운것은?
 - {learn}

{message}


"""

def showAll(entries):
    if not entries:
        print("현재 로그가 없습니다.")
        return
    for e in entries:
        print(e["text"])
        print("\n" + "-" * 30 + "\n")
        

def showByDate(entries, dateStr):
    for e in entries:
        if e["date"] == dateStr:
            print(e["text"])
            return
    print(dateStr + " 에 작성된 로그가 없습니다.")


def addEntry(dateStr):
    entry = log(dateStr)
    appendEntries(entry)


def update(entries, dateStr):
    for e in entries:
        if e["date"] == dateStr:
            e["text"] = log(dateStr)
            saveEntries(entries)
            print(f"{dateStr} 로그를 수정했습니다.")
            return

    print(f"{dateStr}에 작성된 로그가 없습니다.")


def delete(entries, dateStr):
    position = None
    num = 0

    for e in entries:
        if e["date"] == dateStr:
            position = num
        num+=1

    if position is None:
        print(f"{dateStr}에 삭제할 로그가 없습니다.")
        return
    
    del entries[position]
    print(f"{dateStr} 로그를 삭제했습니다.")
    saveEntries(entries)


def search(entries, word):
    wordDates = []
    found = False
    for e in entries:
        if word in e["text"]:
            found = True
            wordDates.append(e["date"])
            parts = e["text"].split("\n\n")
            part1 = parts[1]
            part2 = parts[2]
            if word in part1 and word in part2:
                print(f"**{e["date"]}**\n\n\n{part1}\n\n\n{part2}\n\n\n")

            elif word in part1 and word not in part2:
                print(f"**{e["date"]}**\n\n\n{part1}\n\n\n")
            else:
                print(f"**{e["date"]}**\n\n\n{part2}\n\n\n")
                
    if not found:
        print(f"'{word}'에 대한 검색 결과가 없습니다.")

    
