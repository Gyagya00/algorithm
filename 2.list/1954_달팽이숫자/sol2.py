import sys
sys.stdin = open("input (1).txt")

T = int(input())


for tc in range(1, T+1):
    # N : 달팽이 크기
    N = int(input())
    # N 크기의 달팽이 리스트 벽을 만들었다
    snail = [[0] * N for _ in range(N)]
    # print(N, snail)

    # 델타 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 행, 열 초기설정
    row = 0
    col = 0
    # 델타
    d = 0

    for x in range(1, N*N +1):
        # 행렬의 범위를 벗어나거나 채워진 숫자열을 만나면 방향전환
        # 방향이 한번만 바껴야 하는데...
        if row == N or col == N or snail[row][col] != 0:
            row -= dr[d]
            col -= dc[d]
            d += 1
            if d == 4:
                d = 0
            row += dr[d]
            col += dc[d]

        snail[row][col] = x
        row += dr[d]
        col += dc[d]


    print('#{}'.format(tc))
    for s in snail:
        print(*s)

