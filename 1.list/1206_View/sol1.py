import sys
sys.stdin = open("input.txt")

# 조망권이 확보된 세대 수
# 양쪽 거리 2칸이상

# 풀이
# 내 양쪽 2칸에 길이가 나보다 작은 빌딩 확인
# 4개의 빌딩이 나보다 작다면 작은 애들중에 제일 큰 애랑 나의 빌딩크기차이

def building(arr):
    total_gap = 0
    for i in range(2, b_len-2):
        # 작은 애들 중 가장 큰 애랑 나 차이
        min_gap = 256
        for j in [-2, -1, 1, 2]:
            # 하나라도 나보다 큰 애가 있으면 끝나는 것
            if arr[i] < arr[i+j]:
                min_gap = 0
                break
            # 모두 나보다 작을 때
            # 가운데 빌딩이 다른 빌딩보다 클 때 가장 작은 차이가 나는 애 찾기
            elif arr[i] - arr[i+j] <= min_gap:
                min_gap = arr[i] - arr[i+j]
        # print(min_gap)
        total_gap += min_gap
    return total_gap



for tc in range(1, 11):
    b_len = int(input())
    # 가로 길이
    # 빌딩 높이리스트
    buildings = list(map(int, input().split()))
    print("#{} {}".format(tc, building(buildings)))

