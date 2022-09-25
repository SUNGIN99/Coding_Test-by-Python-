
from typing import List


fairs = [1, 4, 3, 2]

def arrayPairSum_1(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    
    return sum


def arrayPairSum_2(nums: List[int]) -> int:
    sum = 0
    pair = []

    for i, n in enumerate(nums):
        #짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum

def arrayPairSum_3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])