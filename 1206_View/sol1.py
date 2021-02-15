import sys
sys.stdin = open("input.txt")

# 조망권이 확보된 세대 수
# 양쪽 거리 2칸이상

# 풀이
# 내 양쪽 2칸에 길이가 나보다 작은 빌딩 확인
# 4개의 빌딩이 나보다 작다면 작은 애들중에 제일 큰 애랑 나의 빌딩크기차이

def building(n):
    # 5개씩 잘라서 보기
    view = []
    for i in range(T-5):
        # 작은 애들 중 가장 큰 애랑 나 차이
        min_gap = n[i+2] - n[i]
        for j in range(i,i+5):
            if n[i+2] < n[j]:
                min_gap = 0
                break
            # 가운데 빌딩이 다른 빌딩보다 클 때 가장 작은 차이가 나는 애 찾기
            if n[i+2] - n[j] < min_gap and n[i+2] - n[j] > 0:
                min_gap = n[i+2] - n[j]
            # i마다 min_gap
        view.append(min_gap)
    return view



for tc in range(1, 11):
    T = int(input())
    # 가로 길이
    # 빌딩 높이리스트
    buildings = list(map(int, input().split()))
    print(building(buildings))
    print("#{} {}".format(tc, sum(building(buildings))))

