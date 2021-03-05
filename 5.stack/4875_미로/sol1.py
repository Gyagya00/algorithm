import sys
sys.stdin = open("input.txt")

T = int(input())

# 마지막 줄 2에서 출발 0을 따라서 맨 윗줄 3으로 갈 수 있는지
# 풀이방법
# 1. 0을 따라서 길을 가다가
# 2. 모든 방향에 2와 0 둘다 없으면 => 어디에 둬야 하지?
#    저장했었던 갈 수 있었던 길(stack) 중에 방문하지 않은 길을 pop
# 3. 1. 2를 반복한다.
# 4. 0, 2이 없고 stack을 모두 pop해서 확인했을 때 전부 방문한 길일 때 => 도착할 수 없다

# 어려웠던 이유
# 2번을 어떻게 위치시켜야 할지 모르겠었다

#
for tc in range(1, T+1):
    # N 미로의 크기
    N = int(input())
    # 미로 벽을 만들었다!
    miro = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    miro = [[1] * (N+2)] + miro + [[1] * (N+2)]
    # print(miro)
    res = 0

    row = 0
    col = 0

    # 델타 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 경로 저장 스택
    stack = []

    # 3의 위치를 찾는다
    for row in range(N+2):
        for col in range(N+2):
            if miro[row][col] == 3:
                break
        if miro[row][col] == 3:
            break

    stack.append([row, col])

    # 갈 수 있는 길(0, 2)이 있는지 확인하는 함수
    def promising(point):
        # 델타 상 하 좌 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        # 갈 수 있는 길이 있는지
        flag = False
        # 검사할 행, 열
        row = point[0]
        col = point[1]

        for d in range(4):
            if miro[row + dr[d]][col + dc[d]] == 0 or miro[row + dr[d]][col +dc[d]] == 2:
                flag = True
        return flag

    # 실제로 가보자!
    while stack:
        # 현재 미로 위치
        now = stack.pop()
        row = now[0]
        col = now[1]

        # 마지막 줄 2일때
        if miro[row][col] == 2:
            res = 1
            break

        # 방문 표시
        miro[row][col] = 4

        # 갈 수 있는 길이 있다면
        if promising(now):
            # 가자
            for d in range(4):
                # 0이 있는 곳으로 가기
                if miro[row+dr[d]][col+dc[d]] == 0 or miro[row + dr[d]][col +dc[d]] == 2:
                    # 0이 있는 곳은 다 저장
                    stack.append([row+dr[d], col+dc[d]])

        # 갈 수 없다면
        else:
            # 안 가본 길까지 pop
            while stack and miro[now[0]][now[1]] == 4:
                now = stack.pop()


    print("#{} {}".format(tc, res))

