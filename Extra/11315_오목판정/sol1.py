import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

# 5 개 이상이 오목


for tc in range(1, T+1):
    # N 개의 줄 N 개의 문자열
    N = int(input())
    # 오목판
    omok = [list(input()) for _ in range(N)]
    # print(omok)

    # 연속으로 5개 있는지
    five = 'NO'

    # 대각선 확인
    l_cnt = 0
    r_cnt = 0
    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                l_cnt += 1
                r_cnt += 1
                while i < N-1 and j < N-1:
                    i += 1
                    j += 1
                    if omok[i][j] == 'o':
                        l_cnt += 1
                    else:
                        l_cnt = 0
                    if l_cnt == 5:
                        five = 'YES'
                        break
                while i > 0 and j < N-1:
                    i -= 1
                    j += 1
                    if omok[i][j] == 'o':
                        r_cnt += 1
                    else:
                        r_cnt = 0
                    if r_cnt == 5:
                        five = 'YES'
                        break
            if five == 'YES':
                break
        if five == 'YES':
            break


    # 가로 세로 확인
    for j in range(N):
        # 오목 'o' 개수가 5개 인지 확인하려고 센다
        r_omok = 0
        c_omok = 0
        for i in range(N):
            # 가로 확인
            if omok[j][i] == 'o':
                r_omok += 1
            else:
                r_omok = 0
            # 세로 확인
            if omok[i][j] == 'o':
                c_omok += 1
            else:
                c_omok = 0

            if r_omok == 5 or c_omok == 5:
                five = 'YES'
                break
        if five == 'YES':
            break

    print("#{} {}".format(tc, five))

