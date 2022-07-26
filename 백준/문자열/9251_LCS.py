import re

s1 = input()
s2 = input()

char = re.compile('[\w]')

s1_sub1 = char.findall(s1)
s2_sub1 = char.findall(s2)

s1_sub2=[]
s2_sub2=[]

n = 1
for c1 in s1_sub1:
    for c2 in s1_sub1[n:]:
        s1_sub2.append(''.join(c2))
    n+=1

print(s1_sub2)