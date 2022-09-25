import sys

N, M = map(int, input().split())
r, c, d = map(int, input().split())

area = []

for _ in range(N):
    area.append(list(map(int, sys.stdin.readline().strip().split())))

'''

1) 현재 위치를 청소한다.

2) 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
 2-1) 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 
      그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
 
 2-2) 왼쪽 방향에 청소할 공간이 없다면, 
      그 방향으로 회전하고 2번으로 돌아간다.
 
 2-3) 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 
      바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
 
 2-4) 네 방향 모두 청소가 이미 되어있거나 벽이면서, 
      뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

r, c:  시작 좌표 (로봇청소기가 있는 칸의 상태는 항상 빈칸)
d: 방향
{0: 북, 1: 동, 2: 남, 3: 서}

왼쪽 방향 확인
{0: 서, 1: 북, 2: 동, 4: 남}

가로 벽 = 열 -> 값이 0 미만(음수), M 이상
세로 벽 = 행 -> 값이 0 미만(음수), N 이상
빈칸 = 0, 벽 =  1

'''
direction = { # 키(방향) : 값(바라보는 방향 기준 왼쪽)
    0:3, 
    1:0,
    2:1,
    3:2
}

def turnLeft(direct):
    if direct == 0: # 방향 북쪽, 왼방향 서쪽
        stand, move = 'col', -1 # 왼방향과 이동시킬 값(증가 +1, 감소 -1)
        
    elif direct == 1: #방향 동쪽, 왼방향 북쪽
        stand, move = 'row', -1
        
    elif direct == 2: #방향 남쪽, 왼방향 동쪽
        stand, move = 'col', +1
        
    elif direct == 3: #방향 서쪽, 왼방향 남쪽
        stand, move = 'row', +1

    return stand, move

def areaMove(r, c, stand, move, op):
    if op == 1: pass
    else : move = -(move)

    if stand == 'col':
        c += move
    else :
        r += move
    return r, c

def areaOver(r, c):
    if(r >= 0 and r <= N) and (c >= 0 and c <= M) :
        return True
    return False

def checkAllArea(r, c, d):
    north, south = area[r-1][c], area[r+1][c]
    east,   west = area[r][c+1], area[r][c-1]
    if (checkAround(north) and 
        checkAround(south) and 
        checkAround(east) and 
        checkAround(west)):

        stand, move = turnLeft(direction[d])
        r, c = areaMove(r, c, stand, move, 1)

        if checkAround(area[r][c] == 1):
            return r, c, 99
        else :
            # 여기서 문제!
            # r, c 가 반대방향으로 움직였는데 다시 원점으로 안돌아옴!
            r, c = areaMove(r, c, stand, move, 0)

            return r, c, d
    else:
        return False, False, False
        
def checkAround(num):
    if num == 1 or num == -1:
        return True
    return False

def printArea(area):
    for l in area:
        for char in l:
            print(char , end=' ' )
        print()
    print()

point = area[r][c]
cleaned = []
# north, south = area[r-1][c], area[r+1][c]
# east,   west = area[r][c+1], area[r][c-1]
stand, move = None, 0
count = 0
while True:
    # 1) 현재 방을 청소한다.
    if (area[r][c] == 0 and areaOver(r,c)): 
        area[r][c] = -1
        count += 1
    #printArea(area)
    # 2) 현재 위치에서 왼방향을 기준으로 탐색
    stand, move = turnLeft(d)
    # 2-1) 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 
    #      그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    r, c = areaMove(r, c, stand, move, 1)
    if area[r][c] == 0:
        pass
    # 2-2) 왼쪽 방향에 청소할 공간이 없다면, 
    #      그 방향으로 회전하고 2번으로 돌아간다.

    else:
        r, c= areaMove(r, c, stand, move, 0)
        temp_r, temp_c, temp_d = checkAllArea(r, c, d)
        
        if temp_d == 99 :
            break
        elif not temp_r:
            d = direction[d]
        else:
            r, c, d = temp_r, temp_c, temp_d
    #2-3) 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 
    #     바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    #d = direction[d]
        

    #2-4) 네 방향 모두 청소가 이미 되어있거나 벽이면서, 
    #     뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
print(count)