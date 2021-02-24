# 교수님 풀이로 풀어볼거야
import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    # 회문의 길이
    s_len = int(input())
    # 문자판
    board = [list(input()) for _ in range(8)]
    # print(board)
    # 회문의 개수
    cnt = 0

    for i in range(8):
        for j in range(8-s_len+1):
            # 회문인지 비교할 리스트
            r_check = []
            c_check = []
            for k in range(s_len):
                # 회문의 길이만큼 축적
                r_check.append(board[i][j+k])
                c_check.append(board[j+k][i])

            # reverse 하기
            res_check = []
            for idx in range(len(r_check)-1, -1, -1):
                res_check.append(r_check[idx])
            if r_check == res_check:
                cnt += 1
                # print('r', r_check, res_check, i, j)
            # 열탐색전에 reverse 변수 초기화
            res_check = []

            for idx in range(len(c_check)-1, -1, -1):
                res_check.append(c_check[idx])
            if c_check == res_check:
                cnt += 1
                # print('c', c_check, res_check, j, i)

    print("#{} {}".format(tc, cnt))

