import sys
sys.stdin = open("sample_input.txt")

# 최소 충전횟수 구하기
# K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N = 0부터 N번 정류장까지 이동
# M = 충전기가 설치된 정류장 개수


T = int(input())

# 내 위치에서 갈 수 있는 가장 먼 정류장 구하기
def best(fuel, my_stop):
    max_gap = 0
    for i in fuel:
        gap = i - my_stop
        if gap > 3:
            max_gap = 0
        else:
            if gap > max_gap:
                max_gap = gap
    return max_gap

print(best([1, 3, 5, 7, 9], 0))

for tc in range(1, T+1):
    # 각각 변수에 input 넣어주는 것도 어려워..
    k, n, m = map(int, input().split())
    # 충전기가 설치된 정류장
    fuel = list(map(int, input().split()))
    pass
    my_stop = 0
    count = 0
    if best(fuel, my_stop) == 0:
        print("#{} 0".format(tc))
    else:
        while my_stop <= n:
            my_stop += best(fuel, my_stop)
            count += 1
        print("#{} {}".format(tc, count))




















    #
    #
    # # 지금 위치로부터 앞으로 k번 안에 정류장이 있다면 가장 멀리 있는 정류장 (정류장 번호가 가장 큰 것)
    # # 내가 위치한 정류장 번호
    # now_stop = 0
    # # 충전 횟수
    # count = 0
    # # 나랑 충전기 거리 중 max 구하기
    # # 나와 충전기 사이의 거리 모으기
    # for s in stops:
    #     gap = s - now_stop
    #     max_gap = 0
    #
    #     # 나랑 충전기 거리 < 한번 충전인 경우
    #     if gap <= k:
    #         if gap > max_gap:
    #             max_gap = gap
    #     # max_gap만큼 내 위치 이동
    #     now_stop += max_gap
    #     # 충전 한 번 추가
    #     count += 1
    #
    #
    # # 종점에 도착할 수 없는 경우
    # if max_gap == 0:
    #     print("#{} 0".format(tc))
    #
    #     my_stop += max_gap
    #
    #
    #
    #
    #
    # # 지금 정류장에서 k번을 더했을 때 n보다 작거나 같을 때까지
    #
    #
    # print("#{} ".format(tc, ))
    #
