import sys

N, M = map(int, sys.stdin.readline().split())

num_list = []
arrange = {}

for _ in range(0,N):
    num_list.append(int(sys.stdin.readline()))

for _ in range(0,M):
    key , value = map(int, sys.stdin.readline().split())
    arrange[key] = value

#print(num_list)
#print(arrange)

for k in arrange.keys():
    print(min(num_list[k-1: arrange[k]]))

