import sys
sys.stdin = open("input.txt")

T = int(input())

# N * N 행렬
# 90도 180도 270도 회전한 모양 출력

for tc in range(1, T+1):
    # N 행렬의 크기 3 ~ 7
    N = int(input())
    # N * N 행렬
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)

    # 90도 회전시키는 방법
    # 열방향으로 아래부터 읽으면 된다
    def spin_90(m):
        matrix_90 = [[] for _ in range(N)]
        for j in range(0, N):
            for i in range(0, N):
                matrix_90[j].append(m[N-1-i][j])
        return matrix_90


    matrix_90 = spin_90(matrix)
    matrix_180 = spin_90(matrix_90)
    matrix_270 = spin_90(matrix_180)

    # print(matrix_90, matrix_180, matrix_270)

    print('#{}'.format(tc))
    for idx in range(N):
        print(''.join(map(str, matrix_90[idx])), end=' ')
        print(''.join(map(str, matrix_180[idx])), end=' ')
        print(''.join(map(str, matrix_270[idx])), end=' ')
        print()


