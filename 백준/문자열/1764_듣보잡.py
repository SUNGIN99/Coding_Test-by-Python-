'''
듣도 못한 사람의 수 : N
보도 못한 사람의 수 : M

-> 듣도 보도 못한 사람의 명단, 수를 구해야함!

3(N) 4(M)  -첫째줄 듣도못한사람수 N, 보도 못한사람 수 M
ohhenrie    듣도 보도
charlie     듣도 
baesangwook 듣도 보도      --- 듣도못한사람 3(N)명
obama       보도
baesangwook 듣도 보도     -- 보도 모한사람 4(M)명
ohhenrie    듣도 보도
clinton     보도

1) 값 입력
2) 문자열 순서대로입력
3) 리스트 내에 문자열 비교?
    in 함수 = O(n)
    리스트 순회 = O(n) 이므로
    듣도 못한 사람의 리스트 명단을 보도 못한 사람의 리스트 명단에 조회하게 되면 
    O(n^2) 시간이 걸림

4) 위 방법을 하려했으나 해시맵을 사용하면 
    O(n)만큼만 시간복잡도를 줄일 수 있을 것같다.
    딕셔너리를 생성 {
        키(사람의 이름) : 값(리스트)
    }
    해당 키값의 리스트에 사람의 이름마다 값을 하나씩 추가하는 것!

    1 = 듣도 못한사람 ; 2 = 보도 못한 사람
    ex)
    'ohenrie' : [1 , 2]
    'charlie' : [1]
    ... 처럼!

5) 그럼 듣도 보도 못한 사람은 1 2 가 모두 들어가 있으니
    값인 리스트의 길이가 2인 키 값을 따로 빼서 정렬하고 그대로 출력할것
'''

import sys
from typing import List
from collections import defaultdict

input_ = sys.stdin.readline

N, M = map(int, input().split())

unlistened = [] # 듣도 못한 사람 이름 리스트
unseemed = [] # 보도 못한 사람 이름 리스트

for _ in range(N):
    unlistened.append(input_().rstrip())
for _ in range(M):
    unseemed.append(input_().rstrip())

unLS = defaultdict(list) # 듣도 보도 못한 사람 해시맵

def check_Listen_or_Seem(names : List[str], check : int) -> None :
    for name in names:
        unLS[name].append(check)

check_Listen_or_Seem(unlistened, 1)
check_Listen_or_Seem(unseemed, 2)
#print(sorted(unLS.items()))
sorted_unLS = [name for name, lists in sorted(unLS.items())
                            if len(lists) == 2]
#https://blockdmask.tistory.com/566

#print(unLS)
print(len(sorted_unLS))
for name in sorted_unLS:
    print(name)
