#https://leetcode.com/problems/reorder-data-in-log-files/
def Solve(logs):
    letterlog=list()
    digitlog=list()
    for log in logs:
        if log.split()[1].isdigit():
            digitlog.append(log)
        else:
            letterlog.append(log.split())
    letterlog.sort(key=lambda x:x[0])
    letterlog.sort(key=lambda x:x[1:])
    for i in range(len(letterlog)):
        letterlog[i]=" ".join(letterlog[i])
    letterlog.extend(digitlog)
    return  letterlog
logs=["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solve(logs))
