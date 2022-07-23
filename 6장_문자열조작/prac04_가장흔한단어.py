import collections
import re
from typing import List

def mostCommonWord1(paragraph : str, abnned : List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                                    if word not in banned]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    print(counts)

    return max(counts, key = counts.get)


def mostCommonWord2(paragraph : str, abnned : List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                                    if word not in banned]
    
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit Ball flew far after it was hit"
banned = ["hit"]

print(mostCommonWord2(paragraph, banned))