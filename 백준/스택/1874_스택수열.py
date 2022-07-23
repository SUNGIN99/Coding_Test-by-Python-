import sys

n = int(sys.stdin.readline())

nums = [];
stack_list = [];
result = [];

for i in range(0, n, 1):
    nums.append(int(sys.stdin.readline()))

# 4 3 6 8 7 5 2 1
# 1 2 3 4 5 6 7 8

j = 0 ;
i = 1;
while (j < n):

    length = len(stack_list);

    if(length == 0):
        result.append('+')
        stack_list.append(i);
        i = i+1;
        continue;
    
    top = stack_list[length - 1]

    if(top > nums[j] or i>n+1):
        print('NO')
        exit();
    
    elif(top == nums[j]):
        result.append('-')
        #print('-')
        stack_list.pop();
        j = j + 1;

    else:
        result.append('+')
        #print('+')
        stack_list.append(i);
        i = i + 1
    

for r in result:
    print(r)