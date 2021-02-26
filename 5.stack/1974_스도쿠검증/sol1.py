# 1~9 하니씩 들어있는지 확인하는 방법
# 1. visited T/F 로 체크하기
# 2. set 활용하기

import sys
sys.stdin = open("input.txt")

T = int(input())

# 1. 모든 가로 세로줄에 1부터 9까지
# 2. 3 * 3 에 1부터 9까지

for tc in range(1, T+1):
    # 9 * 9 크기의 스도쿠 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # print(puzzle)

    # 결과 정답인지 아닌지
    res = 1

    # 1. 가로 세로 검증
    for i in range(9):
        # 확인할 체크 리스트
        r_check = []
        c_check = []
        for j in range(9):
            r_check.append(puzzle[i][j])
            c_check.append(puzzle[j][i])

        # 겹치는 게 있는지 확인하려고
        # 집합으로 바꾼 뒤에도 개수가 달라지지 않는지 확인
        if len(list(set(r_check))) != 9 or len(list(set(c_check))) != 9:
            res = 0
            break

    # 델타
    # 상 하 좌 우 오하 왼하 오상 왼상
    dr = [-1, 1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, -1, 1, 1, -1, 1, -1]
    # 2. 3 * 3 크기의 작은 격자 검증
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            check = []
            check.append(puzzle[i][j])
            for idx in range(len(dr)):
                row = i
                col = j
                row += dr[idx]
                col += dc[idx]
                if puzzle[row][col] in check:
                    res = 0
                    break
                else:
                    check.append(puzzle[row][col])
            if res == 0:
                break
        if res == 0:
            break


    print("#{} {}".format(tc, res))
