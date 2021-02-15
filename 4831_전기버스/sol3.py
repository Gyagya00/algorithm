# 내가 생각하지 못했던 아이디어!
# k만큼 갈 수 있다는 것을 더하고 빼면서 문제를 푸는 것

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 최소 충전횟수 구하기
# K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N = 0부터 N번 정류장까지 이동
# M = 충전기가 설치된 정류장 개수

def min_charge(k, n, m, fuel_stops):
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
        # 충전 정류소로 가기 전 내 위치
        pre = my_stop

        for i in range(idx, m):
            # 정류장이 k만큼 간 내 뒤에 있어
            if my_stop >= fuel_stops[i]:
                flag = True
                # 그 정류장보다 조금 더 멀리 있는 정류장이 있어?
                # 최대한 멀리 있는 걔로 할래!
                for j in range(m-1, i-1, -1):
                    # 그래도 내 뒤에 있는 거 맞아?
                    if my_stop >= fuel_stops[j]:
                        # 그럼 그 정류장에 돌아가서 충전하자!
                        my_stop = fuel_stops[j]
                        count += 1
                        # 들렸던 정류장은 다시 안 들릴거야
                        idx = j + 1
                        break

                # 더 멀리 있는 애가 없으면 처음 걔로 할래
                if my_stop == pre:
                    my_stop = fuel_stops[i]
                    count += 1
                    idx = i + 1

            # 정류장들이 k만큼 간 나보다 더 앞에 있어
            else:
                # 그럼 나는 더 못가네
                flag = False
                break

    if not flag:
        count = 0

    return count


for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    # 충전기가 설치된 정류장
    fuel_stops = list(map(int, input().split()))

    result = min_charge(k, n, m, fuel_stops)
    print('#{} {}'.format(tc, result))



