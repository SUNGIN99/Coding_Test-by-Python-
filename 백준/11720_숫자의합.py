import sys
input = sys.stdin.readline
#https://hwisaek.tistory.com/entry/Python-sysstdinreadline-%EA%B0%9C%ED%96%89-%EB%AC%B8%EC%9E%90-%EC%B2%98%EB%A6%AC

N = input()
num_str : str = input().strip()
num_list = map(int, num_str)

print(sum(num_list))