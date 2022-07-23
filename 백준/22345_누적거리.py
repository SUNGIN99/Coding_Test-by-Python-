import sys
import math

#input = sys.stdin.readline();

# 1)
# N = 마을의 정보 개수
# Q = 모임 장소 정보 개수
N, Q = map(int, input().split());

a = [];
x = [];
fx = [];
q = [];

# 2)
# 마을 정보 입력(인구 수, 마을 좌표)
for i in range (0, N, 1):
    a_i, x_i = map(int, input().split());
    a.append(a_i);
    x.append(x_i);

# 모임 장소 좌표 입력
for i in range (0, Q, 1):
    q_i = int(input());
    q.append(q_i);

# 3)
howLong = [];

for i in x:
    temp = [];
    for j in q:
        temp.append(abs(i-j))





