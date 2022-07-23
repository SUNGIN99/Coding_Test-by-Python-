import re

# 1) 문자열 입력받기
# 2) 문자열 모두 소문자 or 대문자 둘주 하나로 바꾸기
# 3) 배열 알파벳길이 (26) 중 '알파벳' - '알파벳 아스키값으로 인덱스찾기
# 4) 길이 반환
# 5) 반복문 foreach 이기 때문에 알파벳의 순서 임의로 정해서 대입

# 6) 첫 배열 = 모두 -1 로 초기화

S = list(input())
result = [-1 for _ in range(26)]

# for 
for i in range(len(S)):
    index_ = ord(S[i])-ord('a')
    if(result[index_] == -1):
        result[index_] = i

for i in result:
    print(i, end = ' ')

a = ' '.join(str(x) for x in result)
print(a)

# for each
j = 0
for i in S:
    index_ = ord(i)-ord('a')
    if(result[index_] == -1):
        result[index_] = j
        j += 1
    elif(result[index_] >= 0):
        j += 1


print(result)