from collections import deque


N = int(input())

result = []
cases = []

def maxleftdiff(i : int, maxparam : int, sorted_case):
        left = i - 1;
        
        if(i == 0):
            left = len(sorted_case)-1
        
        left_val = abs(sorted_case[i] - sorted_case[left])
        
        maxleftval = max(maxparam, left_val)
        
        if(i == 0):
            return maxleftval;

        return(max(maxleftval, maxleftdiff(left, maxleftval, sorted_case)))


 
def maxrightdiff(i : int, maxparam : int,sorted_case):
    #print(i)
    right = (i + 1) % (len(sorted_case));

    right_val = abs(sorted_case[i] - sorted_case[right])
    
    maxrightval = max(maxparam, right_val)

    if(i == len(sorted_case)-1):
        return maxrightval;

    return(max(maxrightval, maxrightdiff(right, maxrightval, sorted_case)))


for _ in range(N):
    case_len = int(input())
    testcase = list(map(int, input().split()))

    testcase.sort(reverse = True)

    testcase = deque(testcase)
    sorted_case = deque()

    sorted_case.append(testcase.popleft())

    while len(testcase) >= 1:
        sorted_case.append(testcase.popleft())

        if(len(testcase) == 0) :
            break

        sorted_case.appendleft(testcase.popleft())

    cases.append(sorted_case)

for nums in cases:
    #print(nums)
    maxleftval = maxleftdiff(len(nums) // 2, -1, nums)
    maxrightval = maxrightdiff(len(nums) // 2, -1, nums)

    #print(maxleftval, maxrightval)
    result.append(max(maxleftval, maxrightval))


for i in result:
    print(i)
#print(result)