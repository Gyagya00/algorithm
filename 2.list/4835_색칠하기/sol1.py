import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 겹치는 부분 구하기
# 10 * 10 배열을 만든다
# 해당 구역에 1과 2 더한다
# index 범위를 모서리 정보로 활용
# 3이된 구역을 더한다

for tc in range(1, T+1):
    # 컬러 개수
    N = int(input())
    # 컬러 리스트
    colors = []
    for x in range(N):
        colors.append(list(map(int, input().split())))

    # 10 * 10 배열
    board = [[0] * 10 for _ in range(10)]
    # 배열 인덱스

    for x in colors:
        # x1, x2, y1, y2, color = map(int, input().split()) 으로 하는게 인덱스보다 좋음
        # 각 인덱스 범위 내에 색칠
        for i in range(x[0], x[2] + 1):
            for j in range(x[1], x[3] + 1):
                # 빨강색 (1)은 10의 자리로 더해주고
                if x[4] == 1:
                    board[i][j] += x[4] *10
                # 파랑색 (2) 은 1의 자리로 더해줌
                else:
                    board[i][j] += x[4]

    # 보라색 개수
    cnt = 0
    for x in board:
        for y in x:
            # 각각의 원소가 빨강으로 칠해진 조건 + 파랑으로 칠해진 조건
            if y > 10 and y % 10 > 0:
                cnt += 1

    print("#{} {}".format(tc, cnt))

