import sys
sys.stdin = open("input.txt")

T = 10

# 2차원 배열 각 행, 열, 대각선의 합

for tc in range(1, T+1):
    # 테스트 케이스 번호
    test = int(input())
    # 100 * 100 배열
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 각각의 최댓값 리스트 저장
    max_list = []

    # 행의 합 최댓값
    row_max = 0
    for i in range(100):
        row = 0
        for j in range(100):
            row += arr[i][j]
        if row > row_max:
            row_max = row

    max_list.append(row_max)

    # 열의 합 최댓값
    col_max = 0
    for i in range(100):
        col = 0
        for j in range(100):
            col += arr[j][i]
        if col > col_max:
            col_max = col

    max_list.append(col_max)

    # 대각선의 합
    left_cross = 0
    right_cross = 0
    for i in range(100):
        left_cross += arr[i][i]
        right_cross += arr[i][100-1-i]

    max_list.append(left_cross)
    max_list.append(right_cross)

    # 최댓값 최종 최종
    real_max = 0
    for x in max_list:
        if x > real_max:
            real_max = x

    print("#{} {}".format(tc, real_max))

