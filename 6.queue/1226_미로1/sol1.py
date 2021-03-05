import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc = int(input())
    # 16 * 16 미로
    miro = [list(map(int, input())) for _ in range(16)]
    # print(miro)

    # 델타
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = []
    visited = []
    res = 0

    # 2를 찾자
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                queue.append([i, j])
                visited.append([i, j])
                break
        if queue:
            break

    # print(queue)

    while queue:
        now = queue.pop(0)
        row, col = now

        # 목적지 도착했다
        if miro[row][col] == 3:
            res = 1
            break

        for d in range(4):
            # 방문한 적 없는 길
            if [row+dr[d], col+dc[d]] not in visited and miro[row+dr[d]][col+dc[d]] != 1:
                queue.append([row+dr[d], col+dc[d]])
                # 길이 벌어졌다가 만나는 경우 중복방지
                visited.append([row+dr[d], col+dc[d]])



    print("#{} {}".format(tc, res))

