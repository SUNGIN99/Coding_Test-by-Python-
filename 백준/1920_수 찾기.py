import sys

#N입력
N = int(sys.stdin.readline())
arrN = list(map(int, sys.stdin.readline().split()))
arrN.sort();

#M입력
M = int(sys.stdin.readline())
arrM = list(map(int, sys.stdin.readline().split()))


def b_search(target):
    left = 0;
    right = N - 1;

    while left <= right:
        mid = (left + right) // 2
        if arrN[mid] == target:
            return True
        if target < arrN[mid]:
            right = mid -1
        elif target > arrN[mid]:
            left = mid + 1
    return False


#M검사
for i in arrM:
    if b_search(i):
        print(1)
    else:
        print(0)
    