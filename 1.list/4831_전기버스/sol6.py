# 전기버스문제 최종최종
import sys
sys.stdin = open("sample_input.txt")

T = int(input())


for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_fuel = list(map(int, input().split()))
    # print(bus_fuel)

    # 현재 정류장
    now = 0
    # 현재 충전량
    fuel = K
    # 충전횟수
    cnt = 0
    # 정류장 인덱스
    i = 0

    while now < N:
        # 정류장에 도착할때마다 충전가능
        if i < M and now == bus_fuel[i]:
            # 가장 멀리있는 다음정류장까지 갈 수 있다면
            for j in range(M-1, i-1, -1):
                if bus_fuel[j] - now <= fuel:
                    fuel -= bus_fuel[j] - now
                    now = bus_fuel[j]
                    i = j + 1
                    fuel += K
                    cnt += 1
                    break

        # 한 칸씩 앞으로 간다.
        now += 1
        # 기름도 한 칸씩 줄어든다
        fuel -= 1

        if fuel == -1:
            cnt = 0
            break



    print("#{} {}".format(tc, cnt))

