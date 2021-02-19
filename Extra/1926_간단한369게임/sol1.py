import sys
sys.stdin = open("input (1).txt")

# 3의 배수가 아니라 3, 6, 9가 들어간 숫자

N = int(input())
sams = ['3', '6', '9']

for x in range(1, N+1):
    cnt = 0
    nums = list(str(x))
    for k in nums:
        if k in sams:
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end = ' ')

    if cnt == 0:
        print(x, end = ' ')
