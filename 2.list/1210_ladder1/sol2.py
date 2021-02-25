# 마지막에서 시작하는 걸로! 해보자!
# 델타를 이용하면 에러가 좀 덜 나는 거같아 => 여기서는 경우를 다 나눠야해서 그닥...흠
# 벽도 만들어보자!

import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    t = int(input())
    ladder = []
    # 벽을 만들었다
    for _ in range(100):
        ladder.append([0] + list(map(int, input().split())) + [0])
        # print(ladder)

    # 델타
    # 좌, 상, 우
    dr = [0, -1, 0]
    dc = [-1, 0, 1]

    # 초기설정 행, 열, 방향
    row = 0
    col = 0
    direction = 'up'

    # 마지막 행에 2인 지점 찾기
    for i in range(1, 100):
        if ladder[99][i] == 2:
            # 시작할 지점 저장하기
            row = 99
            col = i
            break

    while row > -1:

        # 좌로 가자
        while ladder[row][col-1] and direction != 'right':
            col -= 1
            direction = 'left'

        # 우로 가자
        while ladder[row][col+1] and direction != 'left':
            col += 1
            direction = 'right'

        row -= 1
        direction = 'up'

        if row == 0:
            # 첫 행에 도착하면 열 출력
            print('#{} {}'.format(tc, col))
            break














