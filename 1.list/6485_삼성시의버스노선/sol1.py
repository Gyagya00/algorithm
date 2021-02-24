import sys
sys.stdin = open("s_input.txt")

T = int(input())


for tc in range(1, T+1):
    # 버스 노선 개수
    N = int(input())
    # 각 버스 노선이 다니는 정류장
    bus = []
    for i in range(N):
        bus.append(list(map(int, input().split())))

    stop_cnt = [0] * 5001

    for point in bus:
        for j in range(point[0], point[1]+1):
            stop_cnt[j] += 1

    # 확인하고 싶은 정류장 개수
    P = int(input())
    # 정류장 번호
    C = []
    for i in range(P):
        C.append(int(input()))

    print('#{}'.format(tc), end=' ')
    for i in C:
        print(stop_cnt[i], end= ' ')

    print()
