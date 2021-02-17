# 시간이 오래걸려서 채점이 안 됨
import sys
sys.stdin = open("input.txt")

T = int(input())

# N일 동안의 매매가 알고있음
# 하루에 최대 1만큼 구입가능, 판매는 얼마든지

# 전날 가격이 다음의 어떤 날보다 싸면 구입
# 순서는 중요 => 정렬을 쓰면 안됨
# 이익이 최대일 때 => 판매 판매가격 - 구입가격 비교해서 구한다

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 최대 이익변수 더한 거 초기화
    sum_profit = 0
    # 전날 가격과 다음의 어떤 날 가격 비교
    for i in range(N):
        # 최대 이익 변수 초기화
        profit = 0
        for j in range(i+1, N):
            # 이익이 발생할 때
            if prices[j] - prices[i] > profit:
                # 최대 이익 계산
                profit = prices[j] - prices[i]

        # 각 인수의 최대 이익을 더해준다.
        sum_profit += profit

    print("#{} {}".format(tc, sum_profit))

