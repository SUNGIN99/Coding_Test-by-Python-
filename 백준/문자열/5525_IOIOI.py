'''
N+1개의 I;
N  개의 O

I와 O가 교대로 나오는 문자열을 P(n)이라 할때

P1 = IOI
P2 = IOIOI
P3 = IOIOIOI
...

input)
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

output)
S에 PN이 몇 군데 포함되어 있는지 출력한다.

ex)
<입력>
1
13
OOIOIOIOIIOII

<출력>
4
OO'IOI'OIOIIOII
OOIO'IOI'OIIOII
OOIOIO'IOI'IOII
OOIOIOIOI'IOI'I

'''

'''
음... 이녀석을 리스트로 나눠서 사용해야 하나??
문자열 사용가능 함수 in, 등등

슬라이싱을 이용한다면??
O(n)의 시간이 걸림!

but n이 너무 큰수라면?? 시간복잡도 줄일 방법은없나...
일단 해보기

'''
N = int(input()) 
M = int(input())
S = input()

# 1) P(n) 생성
I = 'I'
OI = 'OI'

Pn = 'I' + ('OI' * N)  
Pn_len = len(Pn) # 2 * N +1
# C언어로 한다면??
# for (i=0; i<N; i++) { strcat(I, OI); }

#print(Pn)

count = 0; 
i = 0 ; half_of_M = M // 2 - N
while i < (half_of_M):
    rstart = -(i+1)
    rend = rstart - Pn_len

    if(S[rstart:rend:-1] == Pn): # 역방향
        count += 1

    if (S[i:i+Pn_len] == Pn): # 정방향
        count += 1
    
    i = i + 1

#print(i)
if(M % 2 == 1 and S[i:i+Pn_len] == Pn):
    count += 1

print(count)

'''
연속된 O들의 집합을 제거한다면??
OO, OOO 등

# 쓸모없는 인덱스 참조

반반식 탐색하도록 한다면

8 // 2 = 4

[0:4] [4: :-1]
 a  b  c  d  e  f  g  h  i
 0  1  2  3  4  5  6  7  8
-9 -8 -7 -6 -5 -4 -3 -2 -1 

4가 몫이니까
[0:3]   [1:4]   [2:5]   [3:6]   [0:4]
[-1:-4] [-2:-5] [-1:-4] [-1:-4] [-1:-4]

0  1  2  3  4  5  6  7 
-8 -7 -6 -5 -4 -3 -2 -1 

'''

'''
count = 0
i = 0
while i < M-2:
    if(S[i] == 'O'):
        j = S[i:].find('I')
        i = j
    
    if (S[i:i+Pn_len] == Pn):
        count += 1
        i = i + 1

    i = i + 1
'''

