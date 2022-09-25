N = int(input())
stone = list(map(int, input().split()))

remain_stone = [[i] for i in stone]
cnt = N
print(remain_stone)

for i in range(1, N):
    for rs in remain_stone[i-1]:
        if rs < stone[i]:
            remain_stone[i].append(stone[i] - rs)

        elif rs == stone[i]:
            remain_stone[i] = []
            cnt -= 1
            break
        print(rs, remain_stone)
    print()
print(cnt)