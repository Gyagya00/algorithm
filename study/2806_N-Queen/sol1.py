import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 서로 공격하지 못하게 퀸을 놓는 방법의 수
# 같은 행, 열, 대각선 공격가능

# 풀이
# 델타 활용
# 앞에서 사용한 행 열 제외
# 대각선 제외 row + 1, col + 1 으로 -1 -1

for tc in range(1, T+1):
    # N*N : 보드의 크기 N : 퀸의 개수
    N = int(input())

    # 빈 보드
    board = [[0] * N for _ in range(N)]

    # 방법의 수
    cnt = 0

    # 델타
    # 행을 상, 상 대각선으로는 탐색할 필요가 없음
    dr = [1, 0, 0, 1, 1]
    dc = [0, -1, 1, 1, -1]

    # 첫 행의 열세팅
    c = 0

    # 퀸을 위치시키면 1
    # 퀸을 위치시킬 수 있는 구역은 0, 제한구역에는 2

    # 이 반복문에서 뭘 반복할지 정해야해
    # c = 0 일 때, c = 1일 때 ... => c의 이동마다 반복
    while True:

        # 첫 행에서 퀸을 옮겨서 빈보드로 탐색할 조건
        # 1. 맨 마지막 행까지 퀸을 위치시켰을 때
        if 1 in board[N-1]:
            # 빈 보드
            board = [[0] * N for _ in range(N)]
            c += 1
            cnt += 1

        # 첫 행의 퀸이 모든 열을 다 탐색했을 때 종료
        if c == N:
            break

        # 맨 윗 행에 퀸을 위치시키기
        r = 0
        board[r][c]= 1
        # 임시로 사용할 열
        c_tmp = c
        # 첫 행의 퀸 주변을 2로 채우기
        for idx in range(len(dr)):
            while r + dr[idx] < N and r + dr[idx] > -1 and c_tmp + dc[idx] < N and c_tmp + dc[idx] > -1:
                r += dr[idx]
                c_tmp += dc[idx]
                board[r][c_tmp] = 2
            # 행을 2로 다 채우면 원래 퀸 자리로 돌아가서 다시 열 2로 채우기시작
            r = 0
            c_tmp = c


        # 퀸의 위치
        for row in range(1, N):
            for col in range(N):
                # 자리가 빈 자리이면 (0) 1로 채우고
                if board[row][col] == 0:
                    board[row][col] = 1
                    q_row = row
                    q_col = col
                    # 주변을 2로 채운다
                    for idx in range(len(dr)):
                        while row + dr[idx] < N and row + dr[idx] > -1 and col + dc[idx] < N and col + dc[idx]  > -1:
                            row += dr[idx]
                            col += dc[idx]
                            board[row][col] = 2
                        row = q_row
                        col = q_col
                    break
            # 행에 퀸을 위치시킬 구역(0)이 하나도 없을 때
            else:
                # 첫 행을 이동시켜 새로운 보드로 다시 탐색 시작
                c += 1
                board = [[0] * N for _ in range(N)]
                break

    # 틀린 이유!
    # 배열에서 두번째 행부터는 모든 열에 대해서 경우의 수를 따져야 하는데 빼먹었다!
    # 아... 이거 재귀로 풀어야 할 것같다....

    print("#{} {}".format(tc, cnt))

