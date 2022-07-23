from typing import List


def reorderLogFiles(logs : List[str]) -> List[str]:
    letters, digits = [], []
    i = 0
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
        print(i)
        print('letters : ', letters);
        print('digits : ', digits);
        i=i+1

    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    #https://wikidocs.net/64 (lambda 식)
    #https://penguingoon.tistory.com/207 (lambda 식 활용)

    print(i)
    print('letters : ', letters);
    print('digits : ', digits);

    return letters + digits

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

print(reorderLogFiles(logs))