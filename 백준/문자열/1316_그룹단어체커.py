
from typing import List
import sys

N : int = int(input()) # 단어의 개수 N
S : List[str]= [] #N개의 문자열 줄 단어

for _ in range(N):
    S.append(sys.stdin.readline().strip())

'''
1) 알파벳 26개 배열 -1 로 초기화
2) 존재 하지 않는 문자는 -1 
   존재 하는 문자는 0
   문자 그룹이 이어지다가 문자그룹이 아닌 다른 알파벳이 나온다면,
   1 로 변경

   알파벳 26개 배열중 문자를 만낫을때 -1이나 0이 아닌 1로 값이 들어가있으면
   알파벳그룹 문자열 X

   -> 문자열이 그룹문자열이라면 처음부터 끝까지 모두 탐색해야 되는 최소 O(n)의 시간복잡도
   일단 해보겠음...

'''
count = N

for strs in S:
    check = [-1 for _ in range(26)]
    str_list = list(strs)
    post = strs[0]
    
    for char in str_list:
        index_ = ord(char) - ord('a')
        if(char == post and (check[index_] == 0 or check[index_] == -1)): 
        # 연속된 그룹 문자 (처음 탐색하는 문자 또는 연속된 문자)
            check[index_] = 0

        elif (char != post and check[index_] == -1):
        # 그룹문자가 종료되고 새로운 다른 그룹의 문자일 경우
            check[post_index] = 1
            check[index_] = 0

        elif(check[index_] == 1) :
        # 이미 그룹문자가 끝났지만 그룹에서 떨어진 문자일 경우
            count -= 1
            break 
        
        #새로운 문자를 찾을 시에 1로 바꿔주기 위함
        post = char
        post_index = index_

print(count)
            
        


