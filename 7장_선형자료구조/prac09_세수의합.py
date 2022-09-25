

from typing import List

nums = [-1, 0, 1, 2, -1, -4]

#<풀이 1>
def threeSum1(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    #브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        #중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            print(f'i continue: {i}')
            continue
        for j in range(i+1, len(nums) - 1):
            if j > i+1 and nums[j] == nums[j-1]:
                print(f'j continue: {j}')
                continue
            for k in range(j+1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    print(f'k continue: {k}')
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result



# <풀이 2>
# i를 축으로 한다고 함!
def threeSum2(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()


    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1; right = len(nums) - 1;
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0 :
                left += 1
                    
            elif sum > 0 : 
                right -= 1
            else : #sum == 0
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
    return results
            





print(threeSum1(nums))