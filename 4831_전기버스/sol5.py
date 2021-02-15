import sys
sys.stdin = open("sample_input.txt")

T = int(input())


for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    bus_stop = [0] * (N+1)

    # 충전소를 표시하자
    # for i in range(M):
    #     bus_stop[charge] = 1

    for i in charge:
        bus_stop[i] = 1

    bus = 0 # 버스 위치
    ans = 0 # 충전 횟수

    while True:
        # 버스가 이동할 수 있는 만큼 이동을 하자
        bus += K
        if bus >= N : break # 종점을 도착하거나 종점지에서 더 나아간 경우

        for i in range(bus, bus-K, -1):
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus = i
                break

        # 충전기를 못 찾았을 때:
        else: # 여기 else는 for문에 대한 else : 끝까지 반복문을 실행한 이후에 실행된다.
            ans = 0
            break


    print("#{} {}".format(tc, ans))

##########################################################################################

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    ans = 0
    charge = [0] + charge + [N]
    # charge.insert(0,0)
    # charge.append(N)

    last = 0

    # 충전소에 출발점과 도착지를 넣어놓았으므로
    for i in range(1, M+2):
        if charge[i] - charge[i-1] > K:
            ans = 0
            break

        # 갈 수 있으면 아무작업 X
        # 갈 수 없다면 내 바로 직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1

    print('#{} {}'.format(tc, ans))
