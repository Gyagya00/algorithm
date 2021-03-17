import sys
sys.stdin = open("input.txt")

T = 1

for tc in range(1, T+1):
    # 빙고보드 5 5 1~25
    boards = [list(map(int, input().split())) for _ in range(5)]
    # 사회자가 부르는 숫자들
    bingos = []
    for _ in range(5):
        bingos.extend(list(map(int, input().split())))

    # 빙고를 끝내기 위해서
    flag = False

    # 쓸데 없이 반복문 돌지 않으려고
    k = 0

    for num in range(25):
        for i in range(5):
            for j in range(5):
                if boards[i][j] == bingos[num]:
                    boards[i][j] = 0
                    k += 1

                    # 빙고 개수
                    bingo_cnt = 0
                    if k > 11:
                        is_bingo2 = [0, 0]
                        # 빙고 검사하기
                        for i in range(5):
                            # 검사할 리스트
                            is_bingo = [0, 0]
                            for j in range(5):
                                # 가로
                                if boards[i][j] == 0:
                                    is_bingo[0] += 1
                                # 세로
                                if boards[j][i] == 0:
                                    is_bingo[1] += 1
                            # 대각선
                            if boards[i][i] == 0:
                                is_bingo2[0] += 1
                            # 반대각선
                            if boards[i][5-i-1] == 0:
                                is_bingo2[1] += 1

                            for idx in range(2):
                                if is_bingo[idx] == 5:
                                    bingo_cnt += 1
                                if is_bingo2[idx] == 5:
                                    bingo_cnt += 1

                            # print(is_bingo)

                        if bingo_cnt >= 3:
                            flag = True
                            print(num+1)
                            break
            if flag:
                break
        if flag:
            break




