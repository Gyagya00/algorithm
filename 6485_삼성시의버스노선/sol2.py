import sys
sys.stdin = open("s_input.txt")

T = int(input())

for tc in range(1, T+1):
    # 버스 노선 개수
    N = int(input())

    bus_stop = [0] * (5001)

    for i in range(N):
        A, B = map(int, input().split())

        # 해당 정류장에 지나는 버스의 대수 누적
        for j in range(A, B+1):
            bus_stop[j] += 1

    P = int(input()) # 확인하고 싶은 버스 정류장의 수

    print('#{}'.format(tc), end= ' ')
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end= ' ')
    print()