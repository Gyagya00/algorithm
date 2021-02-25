import sys
sys.stdin = open("input.txt")

T = 10
# 아래서(2)부터 타고 올라가면 한번에 끝!
# range 오류를 해결하려면 좌우에 0으로 벽을 만든다

# 사다리타기
# 목적지 2에 도착하는 열번호 구하기
# 방향 전환
# 델타를 활용해서 좌우에 1이 있는지 탐색하기
# 예) 좌에 1이 있으면 그 방향으로 쭉
# 좌로 이동중 좌에 1이 더이상 없으면 or 아래에 1이 생기면 아래로

for tc in range(1, T+1):
    t = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    # 행, 열 인덱스
    row = 0
    col = 0
    start = 0

    # 좌로 갔다가 우로 가면 안되는데 방향을 알려주자
    # 방향 지시자
    direction = 'down'

    while True:
        # 시작열이 0이면 시작 못해 다음 열으로!
        while ladder[0][start] == 0:
            start += 1
            # 시작열 저장
            col = start

        # 좌우를 살펴보자
        # 좌
        while col > 0 and ladder[row][col-1] and direction != 'right':
            # 좌로 이동
            col -= 1
            direction = 'left'
        # 우
        while col < 99 and ladder[row][col+1] and direction != 'left':
            # 우로 이동
            col += 1
            direction = 'right'

        # 아래로 가자
        # 하나만큼 아래로 가자
        row += 1
        direction = 'down'

        # 99행이면 2인지 검사
        if row == 99:
            if ladder[row][col] == 2:
                print("#{} {}".format(tc, start))
                break
            else:
                row = 0
                start += 1




