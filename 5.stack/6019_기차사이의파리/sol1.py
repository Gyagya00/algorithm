import sys
sys.stdin = open("input.txt")

T = int(input())

# 파리가 몇 마일을 이동했을까...?

for tc in range(1, T+1):
    # D 두 기차 전면부 사이의 거리
    # A 기차 A의 속력
    # B 기차 B의 속력
    # F 파리의 속력
    D, A, B, F = map(int, input().split())
    # print(D, A, B, F)

    # 두 기차가 닿을 때까지 걸릴 시간을 구하자
    hour = D /(A+B)

    print("#{} {}".format(tc, F * hour))

