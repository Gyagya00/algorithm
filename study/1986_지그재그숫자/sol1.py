import sys
sys.stdin = open("input (1).txt")

T = int(input())

# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺀다

for tc in range(1, T+1):
    # N 정수
    N = int(input())

    # 계산결과
    res = 0
    for n in range(1, N+1):
        # 홀수이면
        if n % 2:
            res += n
        else:
            res -= n

    print("#{} {}".format(tc, res))

