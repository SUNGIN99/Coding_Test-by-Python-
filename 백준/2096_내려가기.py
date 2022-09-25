'''
1) 갈수 있는 라인에서 최대 / 최소 중 어떻게 진행할지 골라야함
2) 현재있는 별표 위치에 대해서 갈수 있는 범위를 정할것


'''

N = int(input())
lines = []

for _ in range(N):
    lines.append(list(map(int, input().split())))

def checkValidPoint(point):
    # return start, end
    if point == 0:
        return 0, 2
    elif point == 1:
        return 0, 3
    elif point == 2:
        return 1, 3

def returnMin(total, point, level):
    start, end = checkValidPoint(point)
    total += lines[level][point]

    if level == N-1:
        return total 

    elif point == 0:
        return min(returnMin(total, 0, level+1), returnMin(total, 1, level+1))

    elif point == 1:
        return min(returnMin(total, 0, level+1), returnMin(total, 1, level+1), returnMin(total, 2, level+1))

    elif point == 2:
        return min(returnMin(total, 1, level+1), returnMin(total, 2, level+1))

def returnMax(total, point, level):
    start, end = checkValidPoint(point)
    total += lines[level][point]
    
    if level == N-1:
        return total 

    elif point == 0:
        return max(returnMax(total, 0, level+1), returnMax(total, 1, level+1))

    elif point == 1:
        return max(returnMax(total, 0, level+1), returnMax(total, 1, level+1), returnMax(total, 2, level+1))

    elif point == 2:
        return max(returnMax(total, 1, level+1), returnMax(total, 2, level+1))


total_max = returnMax(0, lines[0].index(max(lines[0])), 0)
total_min = returnMin(0, lines[0].index(min(lines[0])), 0)

print(total_max, total_min)


