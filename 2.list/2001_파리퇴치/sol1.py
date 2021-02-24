import sys
sys.stdin = open("input.txt")

T = int(input())

# 가장 많은 파리를 죽이자!

for tc in range(1, T+1):
    # N: 영역의 크기 5~15, M: 파리채의 크기 2~ N
    N, M = map(int, input().split())
    # 파리 개수가 있는 영역 ~30
    space = []
    for _ in range(N):
        space.append(list(map(int, input().split())))

    # 잡은 파리 개수 최댓값
    max_cnt = 0

    # 전체인덱스를 검사하는 대신에
    # 중복 파리채를 빼기 위해서 N-M+1
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            # (0, 0)를 기준으로 파리채 크기 M만큼 이동하면서 파리개수를 더한다
            for r in range(M):
                for c in range(M):
                    cnt += space[i+r][j+c]
            if cnt > max_cnt:
                max_cnt = cnt

    print("#{} {}".format(tc, max_cnt))