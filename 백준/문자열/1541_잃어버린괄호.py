from collections import deque
import re
from typing import List
import numpy

'''
초안
1) 입력 받은 수식 문자열을 - 기호로 split하여 나눈다.
2) -로 나뉜다면 해당 수식을 나눴을 때 최소를 구해야하므로 나뉜 것들끼리 모두 더한다음 음수로 바꿔줌

3) but 모두 + 라서 - 로 바꿀수 없다면??
ex)
10 + 20 - 30 + 40 ->  [10 + 20] , [30 + 40] 
10 + 20 + 30 + 40 -> [10 + 20 + 30+ 40]
10 - 20 + 30 - 40 -> [10], [20 + 30], [40]
10 - 20 - 30 - 40 -> [10], [20], [30], [40]
10+20-30+40

중안
1) 일단 최소를 구해야하기 때문에 음수부호를 이용해 괄호를 치는 것이 관건...
2) 딕셔너리 사용해서 더하기만 할 그룹 '+'
                      빼기만 할 그룹 '-'
    으로 나눠서 식을 나눔
3) 그룹 끼리 + 연산자를 기준으로 split() 하여 나온 리스트를 모두 더하고
4) 각 그룹에 따라서 결과값에 + 또는 -로 전체값을 구함

'''



def returnSum(function : List[str]):
    sumV = 0
    for x in function:
        #print(list(map(int, x.split('+'))))
        nums = list(map(int, x.split('+')))
        sumV += sum(nums)

    return sumV;

waits = {'+' : [],
         '-' : []}

operate = input()

values = operate.split('-')
#print(values)

for op in values:
    key_index = operate.find(op)
    if(key_index == 0):
        waits['+'].append(op)
    else:
        if (operate[key_index - 1] == '+'):
            waits['+'].append(op)
        elif (operate[key_index - 1] == '-'):
            waits['-'].append(op)

    operate = operate.replace(op, 'X', 1)
    #print(operate)
#print(waits)

result = 0
for op, function in waits.items():
    #print(function)
    temp = returnSum(function)
    if op == '+':
        result += temp
    elif op == '-':
        result -= temp
 

print(result)