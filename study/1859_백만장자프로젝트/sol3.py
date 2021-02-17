
import sys
sys.stdin = open("input.txt")

T = int(input())

# N일 동안의 매매가 알고있음
# 하루에 최대 1만큼 구입가능, 판매는 얼마든지

# 스터디
# 전체 최댓값이 아니라 매순간 구간 최댓값을 구해서 이익을 구한다.

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 이익 합
    profit = 0

    # 최대가격
    max_price = 0
    # 뒤에서부터 최대가격을 정한다
    for idx in range(len(prices)-1, -1, -1):
        if prices[idx] > max_price:
            max_price = prices[idx]
        # 구간의 최댓값으로 이익을 구한다
        profit += max_price - prices[idx]


    print("#{} {}".format(tc, profit))

