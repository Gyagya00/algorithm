# 범위자체를 +1, -1해서 변경하는 방법도 있어!
import sys
sys.stdin = open("input.txt")

T = int(input())

# 농장의 크기는 항상 홀수이다.
# 수확은 농장의 크기에 맞는 정사각형 마름모 형태로
# 수확구역의 숫자를 다 합하는 것
# 수확 구역의 인덱스의 규칙을 알아내자

# 인덱스의 규칙
# 맨 가운데는 항상 수확구역 N//2
# 수확구역은 각 행의 행 인덱스 * 2만큼 더해준다


for tc in range(1, T+1):
    # N N 농장의 크기
    N = int(input())
    # 농장 내 농작물의 가치
    farm = [list(map(int, input())) for _ in range(N)]
    # print(farm)

    # 수익
    profit = 0

    # 행
    r = 0

    # 행이 마지막행까지 다 돌았을 때
    while r < N:
        # 중간행까지
        if r <= N//2:
            # 시작 열
            c = N//2 - r
            for k in range(0, 2*r+1):
                profit += farm[r][c+k]
                # print(r, c+k)
        # 중간행부터 끝까지
        else:
            # 시작 열
            c = N//2 - (N-r-1)
            for k in range(0, 2*(N-r-1)+1):
                profit += farm[r][c+k]
                # print(r, c+k)
        r += 1



    print("#{} {}".format(tc, profit))

