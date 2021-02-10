
import sys
sys.stdin = open("sample_input.txt")

# 최소 충전횟수 구하기
# K = 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N = 0부터 N번 정류장까지 이동
# M = 충전기가 설치된 정류장 개수

def bubblesort(n):
    for i in range(len(n)-1, 0, -1):
        for j in range(0, i):
            if n[j] < n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

T = int(input())

for tc in range(1, T+1):
    # 각각 변수에 input 넣어주는 것도 어려워..
    k, n, m = map(int, input().split())
    # print(k,n,m)
    # 충전기가 설치된 정류장
    stops = list(map(int, input().split()))
    # print(stops)

    dis_list = []
    for idx in range(len(stops)-1):
        # 정류장 사이의 거리
        distance = stops[idx+1] - stops[idx]
        dis_list.append(distance)

        if distance > k:
            print("#{} 0".format(tc))
            continue

    # 큰 거리값부터 더해주면 될 거라고 생각했는데
    # 정류장 사이의 거리가 중요한 게 아니라
    # 내 위치와 정류장 사이의 거리가 중요함
    my_stop = 0
    count = 0
    for i in bubblesort(dis_list):
        while my_stop <= n:
            my_stop += i
            count += 1
            # print(my_stop, count)

    print("#{} {}".format(tc, count - 1))


