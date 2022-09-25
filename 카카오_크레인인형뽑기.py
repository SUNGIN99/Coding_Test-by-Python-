#https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    gotchaList = []
    
    for i in moves:
        gotcha = -1
        col = i - 1
        # 1 5 3 5 1 2 1 4
        for level, point in enumerate(board):
            if(point[col] != 0):
                gotcha = point[col]
                print(level, col, point, gotcha)
                point[col] = 0
                break
                
        if(gotcha != -1):
            if(gotchaList and gotchaList[len(gotchaList) - 1] == gotcha):
                gotchaList.pop()
                answer += 2
            else:
                gotchaList.append(gotcha)
        
    
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

for i in board:
    print(i)
print(solution(board, moves))
for i in board:
    print(i)

# 4 3 1 1 3 2 