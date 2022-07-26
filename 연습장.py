a = 'abcdefgh'

for i in range(3):
    print('정순', i, i+3 ,a[i:i+3])
    rstart = -(i+1)
    rend = rstart - 3

    print('역순', rstart, rend, a[rstart:rend:-1])

