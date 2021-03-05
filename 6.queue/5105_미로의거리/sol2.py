import sys
sys.stdin = open("input.txt")

from collections import deque
T = int(input())

# 최소(bfs)한의 칸 수, 없는 경우 0
# 틀린이유
# 1. 출발, 도착 첫줄, 마지막줄 아님

for tc in range(1, T+1):
    # N 미로의 크기
    N = int(input())
    # 미로정보 벽쌓은
    miro = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    miro = [[1] * (N+2)] + miro + [[1] * (N+2)]
    # print(miro)

    # 시작점
    queue = []
    visited = []
    # 지나온 0의 개수
    lengths = [0]
    # 2에 도착했을 때 결과
    res = 0

    # 시작점의 열을 찾기
    for i in range(N+2):
        for j in range(N+2):
            if miro[i][j] == 2:
                queue.append([i, j])
                visited.append([i, j])
                break
        if queue:
            break


    # 델타 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    deq = deque(queue)

    while deq:
        now = deq.popleft()
        row, col = now

        zero = lengths.pop(0)

        # 도착확인
        if miro[row][col] == 3:
            res = zero - 1
            break

        # 큐 쌓기
        for d in range(4):
            if [row+dr[d], col+dc[d]] not in visited and miro[row+dr[d]][col+dc[d]] != 1:
                deq.append([row+dr[d], col+dc[d]])
                visited.append([row+dr[d], col+dc[d]])
                lengths.append(zero+1)
                # print(queue, zero)

    print("#{} {}".format(tc, res))

