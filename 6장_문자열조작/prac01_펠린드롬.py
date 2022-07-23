# 주어진 문자열이 펠린드롬인지 확인하라.
# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# 입력 1 : "A man, a plan, a canal: Panama"
# 출력 1 : True

# 입력 2 : "race a car"
# 출려 2 : false


# 풀이 1 : 리스트로 변환하여 판별
import collections
import re
from typing import Deque


def isPalindrome1(s: str)-> bool:
    strs = []
    for char in s:
        if char.isalnum(): #isalnum : 문자열이 문자 또는 숫자라면 참
            strs.append(char.lower())

    # 펠린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False;

    return True;


# 풀이 2 : 데크 자료형을 이용하여 최적화
def isPalindrome2(s : str) -> bool:
    #자료형 데크
    strs : Deque = collections.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
# 리스트의 pop(0) 은 O(n)만큼 시간 이 걸림
# deque의 popleft() 는 O(1)만큼 시간 걸림ㄷ
# 프로그램 n번 반복시 리스트 = O(n^2) , 데크 = O(n)


def isPalindrome3(s :str) -> bool:
    s = s.lower() #모두 소문자로 변환

    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '' , s)
    # sub(패턴, 교체할문자, 문자열)
    # 소문자 알파벳과 숫자가 아닌 모든 문자를 '' 로 바꾼다 s에서
    # https://brownbears.tistory.com/506 (re = regular expression)

    return s == s[::-1]
    # s[::-1] 문자열 뒤집기 
    # 처음부터 끝까지 -1 간격으로 (역순으로)
