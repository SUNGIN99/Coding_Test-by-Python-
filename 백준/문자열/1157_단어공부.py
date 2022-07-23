
import collections
# 1) 문자열 입력 받고 대문자로 모두 변환 upper 케이스
# 2) 카운터 딕셔너리 사용하여 개수 출ㄹ력
# 3) most_common() 함수 사용하여 
#   3-1) 문자열이 한글자면 해당 글자가 제일 많으므로 바로 출력
#   3-2) 문자열이 두글자 이상이면 첫번째로 많은 글자와 
#                                두번째로 많은 글자의 개수가
#        (if)같다면, ? 출력 
#        (else)아니라면 첫번째로 많은 글자의 문자 출력

S = input().upper()

count_abc = collections.Counter(S)

max_num = count_abc.most_common()
print(max_num)

if(len(count_abc) == 1):
    print(max_num[0][0])

else:
    if(max_num[0][1] == max_num[1][1]):
        print('?')
    else:
        print(max_num[0][0]) 

