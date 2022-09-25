

import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    print(anagrams)

    for word in strs :
        anagrams[''.join(sorted(word))].append(word)
        print(anagrams)
        #https://blockdmask.tistory.com/468
    
    return list[anagrams.values()]

 


a = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(a))
