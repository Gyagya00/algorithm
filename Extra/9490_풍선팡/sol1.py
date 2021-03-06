import sys
sys.stdin = open("input1.txt")

T = int(input())

# 풍선이 M개씩 N개의 줄에
# 어떤 풍선을 터트리면 꽃가루개수만큼 상하좌우로 풍선이 더 터진다
# 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합의 최대값

# 틀린 이유
# 1. 행열 초기화 위치
# 2. 최대 꽃가루 개수를 구하는 위치 설정

for tc in range(1, T+1):
    # N행, M열
    N, M = map(int, input().split())
    # flower 꽃가루의 개수가 적힌 행렬
    flower = [list(map(int, input().split())) for _ in range(N)]

    # 델타
    # 상 하 우 좌
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 최대 꽃가루 합
    max_sum = 0
    for i in range(N):
        for j in range(M):
            # 각 위치별 꽃가루의 합
            flower_sum = 0
            # 내 위치 꽂가루 더하고
            flower_sum += flower[i][j]
            # 상하좌우 꽃가루를 더하기
            for idx in range(4):
                # 기준 행, 열 초기화
                row = i
                col = j
                # 내 위치의 꽃가루 개수만큼 상하좌우이동
                for _ in range(flower[i][j]):
                    row += dr[idx]
                    col += dc[idx]
                    # 인덱스 에러
                    if row > N-1 or row < 0 or col > M-1 or col < 0:
                        break
                    # 상하좌우 꽃가루 더하기
                    flower_sum += flower[row][col]

            # 최대 꽂가루 개수 구하기
            if flower_sum > max_sum:
                max_sum = flower_sum

    print("#{} {}".format(tc, max_sum))

