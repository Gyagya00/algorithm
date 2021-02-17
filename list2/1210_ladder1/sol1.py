import sys
sys.stdin = open("input.txt")

T = int(input())

# 사다리타기
# 목적지 2에 도착하는 열번호 구하기
# 방향 전환
# 델타를 활용해서 좌우에 1이 있는지 탐색하기
# 예) 좌에 1이 있으면 그 방향으로 쭉
# 좌로 이동중 좌에 1이 더이상 없으면 or 아래에 1이 생기면 아래로

for tc in range(1, T+1):
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    # 행, 열 인덱스
    row = 0
    col = 0

    # 시작 열
    start = 0

    while True:
        if ladder[row][col] == 2:
            break

        # 시작열이 0이면 시작 못해 다음 열으로!
        if ladder[0][start] == 0:
            start += 1
            continue

        # 좌우 탐색
        while ladder[row][col+1] or ladder[row][col-1]:
            # 오른쪽에 길이 있으면
            if ladder[row][col+1]:
                # 그 길로 이동
                col += 1
                # 그 오른쪽에 길이 없으면 끝
                if ladder[row][col+1] == 0 or col == 99:
                    print(row, col)
                    break

            # 왼쪽에 길이 있으면
            elif col > 0 and ladder[row][col-1]:
                col -= 1
                if ladder[row][col-1] == 0 or col == 0:
                    print(row, col)
                    break

        # 좌우에 길이 없으면
        row += 1

        # 다 돌았는데 마지막이 1일 때
        if row == 99 and ladder[row][col] == 1:
            start += 1
            break

    print("#{} {}".format(tc, start))

