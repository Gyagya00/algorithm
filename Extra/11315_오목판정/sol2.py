# 5개 후에 있는 돌이 범위안에 있는지 확인하는 아이디어!
import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())



for tc in range(1, T+1):
    # N 개의 줄 N 개의 문자열
    N = int(input())
    # 오목판
    omok = [list(input()) for _ in range(N)]


    # 델타
    # 하 우 정대 반대
    dr = [1, 0, 1, 1]
    dc = [0, 1, 1, -1]

    # 오목성공 여부
    flag = False


    for row in range(N):
        for col in range(N):
            if omok[row][col] == 'o':
                # 델타만큼 이동
                for k in range(4):
                    r = row
                    c = col
                    # 한번 제외 => 4번 반복
                    for _ in range(4):
                        r += dr[k]
                        c += dc[k]
                        # 인덱스 에러방지
                        if r >= N or c >= N or r <= -1 or c <= -1:
                            break
                        if omok[r][c] != 'o':
                            break
                    else:
                        flag = True
                        break
                if flag:
                    break
        if flag:
            break

    if flag:
        print("#{} YES".format(tc))
    else:
        print("#{} NO".format(tc))
