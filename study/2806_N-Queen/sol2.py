# 재귀함수를 써보자
import sys
sys.stdin = open("input.txt")

T = int(input())

# c: 첫행의 열, cnt: 개수, p_row: 이전 행 기억, p_col: 이전 열 기억
def queen(c, cnt, p_row, p_col):




for tc in range(1, T+1):
    # N*N : 보드의 크기 N : 퀸의 개수
    N = int(input())

    # 빈 보드
    board = [[0] * N for _ in range(N)]

    # 방법의 수
    cnt = 0

    # 델타
    # 행을 상, 상 대각선으로는 탐색할 필요가 없음
    dr = [1, 0, 0, 1, 1]
    dc = [0, -1, 1, 1, -1]

    # 첫 행의 열세팅
    c = 0

    print("#{} ".format(tc, ))

