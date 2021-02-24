# 내가 생각하지 못했던 아이디어!
# k만큼 갈 수 있다는 것을 더하고 빼면서 문제를 푸는 것

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 최소 충전횟수 구하기
# K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N = 0부터 N번 정류장까지 이동
# M = 충전기가 설치된 정류장 개수


for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    # 충전기가 설치된 정류장
    fuel_stops = list(map(int, input().split()))

    # 내 위치
    my_stop = 0
    # 충전 횟수
    count = 0
    # 갈 수 있는지 없는지 표시
    flag = False
    # idx번째  정류장
    idx = 0
    # 내 위치가 종점을 안 지나칠 때까지 while
    while my_stop <= n:
        # k만큼 갔어
        my_stop += k

        # 멀리 있는 정류장 중에 내가 갈 수 있는 정류장 찾기
        for i in range(m-1, idx+1, -1):
            # 정류장들이 다 k만큼 간 나보다 더 앞에 있어
            if my_stop < fuel_stops[i]:
                # 그럼 나는 더 못가네
                flag = False

        # 멀리 있는 정류장 중에 내가 갈 수 있는 정류장 찾기
        for i in range(m - 1, idx + 1, -1):
            # 뒤에 있는 정류장중에 제일 큰 애로 할께!
            my_stop = fuel_stops[i]
            count += 1
            flag = True
            print(my_stop, count)
            break

        # 갔던 애들은 빼줘야지
        idx = i + 1

    if flag:
        print("#{} {}".format(tc, count))

    else:
        print("#{} 0".format(tc))



