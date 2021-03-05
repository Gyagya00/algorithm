import sys
sys.stdin = open("input.txt")

T = int(input())

# N * N 배열
# 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소
# 가로로 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다!

# 문제풀이
# 열방향 탐색
# 해당 열에서 최소를 구해서 다 더하면 최소합 => 아니네...흠
## 틀린이유!
# 가로 세로로 1개 씩만 고를 수 있다


for tc in range(1, T+1):
    # N * N 배열
    N = int(input())
    # 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    min_total = 10 * N

    for x in range(N):
        # 방문한 행 열
        visited = [[], []]

        if dfs([0, x], 0) < min_total:
            min_total = dfs([0, x], 0)

    def dfs(start, total = 0):
        global visited

        row, col = start
        total += arr[row][col]

        visited[0].append(row)
        visited[1].append(col)

        # 모든 경우의 수
        for k in range(0, N):
            # visited 확인
            if k not in visited[1]:
                dfs([row + 1, k], total)
                visited[0].pop()
                visited[1].pop()








    print("#{} ".format(tc, ))

