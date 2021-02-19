import sys
sys.stdin = open("input (1).txt")

T = int(input())

# 행탐색, 열탬색으로 연속된 k개의 1을 찾는다
# 하지만 k를 넘으면 제외
# 틀린 이유
# 한 행, 한 열 내에 연속된 k개의 1이 여러개일 가능성 고려!!

for tc in range(1, T+1):
    # N :퍼즐 크기, K :단어의 길이
    N, K = map(int, input().split())
    # 퍼즐
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    # 단어가 들어갈 수 있는 자리의 수
    cnt = 0

    # 행방향 K번 연속된 흰부분 개수 구하기
    for i in range(N):
        white = 0
        for j in range(N):
            if puzzle[i][j]:
                white += 1
                # K개 연속이면 cnt에 1추가
                if white == K:
                    cnt += 1
                # K개 넘게 연속이면 다시 cnt -1
                if white == K+1:
                    cnt -= 1
            else:
                white = 0

    # 열방향 K번 연속된 흰부분 개수 구하기
    for i in range(N):
        white = 0
        for j in range(N):
            if puzzle[j][i]:
                white += 1
                # K개 연속이면 cnt에 1추가
                if white == K:
                    cnt += 1
                # K개 넘게 연속이면 다시 cnt -1
                if white == K+1:
                    cnt -= 1
            else:
                white = 0



    print("#{} {}".format(tc, cnt))

