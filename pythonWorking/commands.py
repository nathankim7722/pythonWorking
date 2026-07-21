
from datetime import date, timedelta
from storage import loadEntries, saveEntries, appendEntries, saveJson


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
    found = []
    
    for e in entries:
        if word in e["text"]:
            print('\n\n\n')
            print(f"{e["text"]}\n\n\n")
            found.append(e)

    if not found:
        print(f"'{word}'에 대한 검색 결과가 없습니다.")

    return found


def stats(entries):
    length = len(entries)
    
    if length==0:
        print("작성된 로그가 없습니다.")
    else:
        print(f"총 업무 기록 : {length}건")

    dates = [e["date"] for e in entries]

    firstDate = min(dates)
    lastDate = max(dates)

    print("가장 오래된 기록: " + firstDate)
    print("가장 최근 기록: " + lastDate)

    today = date.today()
    dayMinusSeven = today - timedelta(days=7)
    daysWorked = 0

    for e in entries:
        entryDate = date.fromisoformat(e["date"])
        if dayMinusSeven <= entryDate:
            daysWorked+=1

    print(f"최근 7일 기록 : {daysWorked}건")

    topWords = {}

    for e in entries:
        parts = e["text"].split("\n\n")
        work = parts[1].split("\n", 1)[1].strip().lstrip("- ").strip()
        learn = parts[2].split("\n", 1)[1].strip().lstrip("- ").strip()

        workAndLearn = work + " " + learn
        words = workAndLearn.replace("\n", " ").split(" ")
        for word in words:
            word = word.strip()
            if not word:
                continue
            topWords[word] = topWords.get(word, 0) + 1

    sortedWords = sorted(topWords.items(), key=lambda num: num[1])
    top5 = sortedWords[-5:]
    top5 = top5[::-1]

    print("\n자주 등장한 단어: ")
    for word, count in top5:
        print(f"{word} ({count}번)")


def export(entries):
    saveJson(entries)
    print("pythonWorking.json를 Export했습니다.")






