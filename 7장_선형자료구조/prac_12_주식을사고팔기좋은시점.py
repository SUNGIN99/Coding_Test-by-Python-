from typing import List

from numpy import average
import sys

def maxProfit_2(prices: List[int]) -> int:
    max_price = 0

    middle = len(prices) // 2

    low_point = min(prices[0:middle])
    high_point = max(prices[middle:])

    return high_point - low_point

def maxProfit_3(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit

# 주식 -> 값이 언제 오르고 언제 내릴지 모름...
# 차가 최대로 값을 가질 수 있는 두 인덱스를 찾아야함.
# 기본적으로 인덱스를 탐색해야하는데 n^2 시간은 걸리기 싫음
# 2차원 문제라고 생각햇을때
# 시점 : 인덱스 ,   값 : 가격
# 투포인터는 중앙으로 값을 이동시키기에는 정렬되어있지 않기때문에 불가능할 것 같음
# 차이는 반드시 오른쪽에 있는 값에서 왼쪽에 있는 값을 빼야함!


cells1 = [7, 1, 5, 3, 6, 4] # 6    6 //2 = 3
cells2 = [7, 1, 5, 3, 6, 4, 6] # 7     6 // 2= 3
celss3 = [2, 8, 1, 6]

print(maxProfit_3(celss3))

# 평균 값을 구하고 가장 차이가 많이나는 최저점과 고점을 찾는다면?