# 문자열을 뒤집는 함수를 작성하라. 
# 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

# ['h', 'e', 'l', 'l', 'o']
# ['o', 'l', 'l', 'e', 'h']

# 풀이 1 : 투 포인터를 이용한 스왑
from typing import List


def reverseString_1(s : List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 풀이 2 : 파이썬 다운 방식
def reverseString_2(s : List[str]) -> None:
    s.reverse()

    # s[:] = s[::-1]