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

    # 사용할 수 있는 열 인덱스
    stack = []

    # 최소합
    min_sum = 0
    for i in range(N):
        min_col = 10
        for j in range(N):
            if arr[i][j] < min_col:
                min_col = arr[i][j]
        min_sum += min_col

    print("#{} {}".format(tc, min_sum))

