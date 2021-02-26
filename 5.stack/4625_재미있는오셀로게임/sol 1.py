import sys
sys.stdin = open('input.txt')

T = int(input())

# 보드에 돌의 개수가 많은 플레이어가 승리한다.
# 가로 세로 대각선!!! 대각선 빼먹음
# 틀린 이유
# 사이 : 하나 건너서가 아니다 끝과 끝이 같은 색이기만 하면됨

for tc in range(1, T+1):
    # N 보드의 한변의 길이, M 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split())
    # 돌을 놓을 위치, 돌의 색
    stone_list = [list(map(int, input().split())) for _ in range(M)]
    # print(stone_list)

    # 돌을 놓을 바둑판
    # 벽도 만들었어
    board = [[0] * (N+2) for _ in range(N+2)]
    # 기본 바둑 돌을 깔자
    board[N // 2][N // 2] = 2
    board[N // 2][N // 2 + 1] = 1
    board[N // 2 + 1][N // 2 + 1] = 2
    board[N // 2 + 1][N // 2] = 1
    # print(board)

    # 상하좌우대각선델타
    dr = [-1, 1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, -1, 1, 1, -1, 1, -1]

    # 흑 백
    color = [1, 2]

    for stone in stone_list:
        for idx in range(2):
            # 흑을 놓을 때
            if stone[2] == color[idx]:
                # 흑을 놓고
                board[stone[0]][stone[1]] = color[idx]
                # 상하좌우에 바꿀 흰돌을 찾는다
                for d in range(8):
                    # 현재 위치 초기화
                    row = stone[0]
                    col = stone[1]
                    row += dr[d]
                    col += dc[d]
                    # 상하좌우에 있는게 흰색
                    while board[row][col] == color[1-idx]:
                        row += dr[d]
                        col += dc[d]
                        # 그 끝에 흑색이 있을 때
                        if board[row][col] == color[idx]:
                            # 반대로 거슬러 올라가서 흑색으로 바꿔주기
                            row -= dr[d]
                            col -= dc[d]
                            while board[row][col] == color[1-idx]:
                                board[row][col] = color[idx]
                                row -= dr[d]
                                col -= dc[d]

    # print(board)
    # 1세기
    cnt_1 = 0
    # 2세기
    cnt_2 = 0
    for x in board:
        cnt_1 += x.count(1)
        cnt_2 += x.count(2)

    print('#{} {} {}'.format(tc, cnt_1, cnt_2))