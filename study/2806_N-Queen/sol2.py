# 재귀함수를 써보자
import sys
sys.stdin = open("input.txt")

T = int(input())

# 재귀함수로 반복해야 될 것이 무엇인가?
# row, col 자리를 이동한 채 모든 경우의 수를 찾는 것

# cnt: 개수, c: 첫행의 열, row: 행, col: 열
def queen(cnt = 0, row = 0, col = 0):
    # 빈 보드
    board = [[0] * N for _ in range(N)]

    # 델타
    dr = [1, 0, 0, 1, 1]
    dc = [0, -1, 1, 1, -1]

    # 첫행의 마지막 열까지 퀸을 놓은 채로 함수가 돌면
    if board[0][N-1] == 1 :
        return cnt

    # 마지막 행에 1이 놓이면 cnt + 1
    if 1 in board[N-1]:
        cnt += 1

    # 자리가 0이면 퀸 위치
    if board[row][col] == 0:
        board[row][col] = 1
        # 다음 퀸을 놓을 수 없는 구역을 2로 바꾸기
        for d in range(5):
            while True:
                row += dr[d]
                col += dc[d]
                board[row][col] = 2
                # index 벗어나기 전 while문 끝내기
                if row < N-1 and col < N-1 and col > 1:
                    break
    # 아니면 다음 열 탐색
    else:
        col += 1
        return queen(cnt, row, col)

    # 첫번째 행 첫번째 열 처리한 뒤 다음 행으로 이동해서 반복
    row += 1
    return queen(cnt, row, col)

    # 열 위치를 바꾸면서 반복하는 걸 어떻게 하지?

























    # 맨 끝까지 탐색했을 때 재귀함수 끝!
    if c == N:
        return cnt

    # 퀸의 위치
    for row in range(N):
        for col in range(N):
            # 자리가 빈 자리(0)이면 1로 채우고
            if board[row][col] == 0:
                board[row][col] = 1
                q_row = row
                q_col = col
                # 주변을 2로 채운다
                for idx in range(len(dr)):
                    while row + dr[idx] < N and row + dr[idx] > -1 and col + dc[idx] < N and col + dc[idx] > -1:
                        row += dr[idx]
                        col += dc[idx]
                        board[row][col] = 2
                    row = q_row
                    col = q_col
                break



for tc in range(1, T+1):
    # N*N : 보드의 크기 N : 퀸의 개수
    N = int(input())


    # 방법의 수
    cnt = 0

    # 첫 행의 열세팅
    c = 0

    print("#{} ".format(tc, ))

