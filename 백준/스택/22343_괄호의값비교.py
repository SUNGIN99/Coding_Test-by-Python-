def isValid(s: str):
    stack = []
    sum = 0
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    X = 1; check = 0
    #스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            X = 1
            if(stack or check == 0):
                X = 2
            
            stack.append(char)
            
        else :
            top = stack.pop()
            
            if(table[char] == top):
                sum += 1 * X
                check = 1



        #elif not stack or table[char]!= stack.pop():
        #    return False

    print(sum)
    return sum
'''
괄호빼는건 문제없는데 1이냐 아니면 *2 를 해줘야하느냐의 차이인데
어떻게 구분할지를 생각해보자

(( 여는 괄호가 두개 동시에 들어오면 *2를 반드시 해줘야한다
(  하나만 들어오면 그저 1?


'''


T = int(input())
result = []

for _ in range(T):
    A = input()
    B = input()
    if(isValid(A) == False or isValid(B) == False ): exit
    elif(isValid(A) > isValid(B)): result.append('>')
    elif(isValid(A) == isValid(B)): result.append('=')
    else: result.append("<")

for c in result:
    print(c)
