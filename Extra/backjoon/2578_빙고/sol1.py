import sys
sys.stdin = open("input.txt")

T = 1

# 사회자가 부른 숫자를 0으로 바꾼다
# 가로 세로 대각선이 다 0인것을 확인한다


for tc in range(1, T+1):
    # 빙고보드 5 5 1~25
    boards = [list(map(int, input().split())) for _ in range(5)]
    # 사회자가 부르는 숫자들
    bingos = []
    for _ in range(5):
        bingos.extend(list(map(int, input().split())))


    def bingo_number(board, bingo):
        k = 0
        # 빙고 리스트
        bingo_list = []
        for idx in range(25):
            for i in range(5):
                for j in range(5):

                    # 사회자가 부른 숫자를 0으로 바꿔줌
                    if board[i][j] != bingo[idx]:
                        continue
                    else:
                        board[i][j] = 0

                    if k > 4:

                        # 가로확인
                        if board[i] == [0] * 5:
                            if [i, 0] not in bingo_list:
                                bingo_list.append([i, 0])

                        # 세로확인
                        for row in range(5):
                            if board[row][j] != 0:
                                break

                        else:
                            if [0, j] not in bingo_list:
                                bingo_list.append([0, j])

                        # 대각선 확인
                        for d in range(5):
                            if board[d][d] != 0:
                                break

                        else:
                            if [1, 1] not in bingo_list:
                                bingo_list.append([1, 1])

                        # 반대 대각선
                        for d in range(4):
                            if board[d][4-d] != 0:
                                break


                        else:
                            if [-1, -1] not in bingo_list:
                                    bingo_list.append([-1, -1])

                        if len(bingo_list) > 2:
                            return idx + 1

    print(bingo_number(boards, bingos))

