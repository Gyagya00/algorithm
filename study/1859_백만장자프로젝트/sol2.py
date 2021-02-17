# 뒤에서부터 하면 시간복잡도가 줄어든다고 해서
# 뒤에서부터 하는 것 장점
# 인덱스가 안 바뀜
# 시간 복잡도가 줄어든다.
import sys
sys.stdin = open("input.txt")

T = int(input())

# N일 동안의 매매가 알고있음
# 하루에 최대 1만큼 구입가능, 판매는 얼마든지

# 댓글 참고함
# 1. 배열중 가장 큰 값을 찾고 그 값보다 앞에 있는 값들과 차이만큼 결과값에 ++ 합니다.
# 2. 그 후, 가장 큰 값과 앞에 있는 값들을 모두 배열에서 제외한 새로운 배열을 만듭니다.
# 배열의 크기가 0이나 1이 될 때까지 1, 2 반복

# 판매가격 중 가장 큰 것을 찾는다
# 그 기준으로 그보다 앞에 있는 구매가격과의 차액
# 이익을 더하고 배열에서 제외한다.

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 이익 합
    profit = 0

    while True:
        # prices가 비거나 비교대상이 없으면 끝
        if len(prices) < 2:
            break

        # 최대 판매가격 초기화
        sell = 0
        idx = 0
        # 최대 판매가격 구하기
        for i in range(len(prices)):
            if prices[i] > sell:
                sell = prices[i]
                idx = i

        # 판매가격보다 앞에 있는 구매가격과의 차이 (= 이익) 적립하기
        for j in range(idx, -1, -1):
            profit += sell - prices[j]
            # 해당 원소 없애기 & 최댓값까지 없애기
            del prices[j]

        # 새로운 리스트로 반복

    print("#{} {}".format(tc, profit))

