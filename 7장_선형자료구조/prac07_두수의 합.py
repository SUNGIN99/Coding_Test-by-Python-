# Q 07 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스르 리턴하라.
from typing import List


nums = [2, 7, 11, 15]
target = 9

nums_map = {}
for i, num in enumerate(nums):
    nums_map[num] = i

print(nums_map)
print(1 in nums_map)
print(7 in nums_map)



# 출력 = [0, 1]

'''
풀이1) 브루트 포스로 계산
배열을 2번 반복하여 모든 조합을 더해보고 일일이 확인해보는 
무차별 대입방식 = 브루트포스(Brute-Force)

=> 굉장히 비효율적

시간 복잡도 = O(n^2) 가 될것임 (1/2*(n^2))  but 상수 안따지니까
지나치게 느리다!

'''
def twoSum_1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]



'''
풀이2) in을 이용한 탐색
시간복잡도 O(n)

'''
def twoSum_2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

def twoSum_3(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 뒤집어서 딕셔너리로 저장
    for i, n in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
        #뺀 값이 key로 존재하는지, 그리고 그 값이 서로 다른 값인지
            return [i, nums_map[target - num]]


def twoSum_4(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    
    #하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num] , i]
        nums_map[num] = i

def twoSum_4(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) -1
    
    while not left == right:
        #합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        
        #합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1

        else :
            return[left, right]

    print('리스트내에 존재 X')