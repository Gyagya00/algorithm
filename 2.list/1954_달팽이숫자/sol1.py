import sys
sys.stdin = open("input (1).txt")

T = int(input())

# 달팽이는 N * N

# 풀이
# 인덱스 변화 보기 => (0,0) (0,1) (0,2)  열 증가 (1,2) (2,2) 행 증가 (2,1) (2,0) 열 감소 (1,0) 행 감소(1,1) 열 증가
# 바깥에 큰 네모의 법칙 -2 인채로 내부 작은 네모 반복

for tc in range(1, T+1):
    # N : 달팽이 크기
    N = int(input())
    # N 크기의 달팽이 리스트
    # snail = [[0] * N] * N 얕은 복사로 [[0 <- 얘랑, 0], [0 <- 얘가, 0]] 같은 인덱스를 쓴다
    snail = [[0] * N for _ in range(N)]
    # 행 열 인덱스
    r_start = 0
    r_end = N
    c_start = 0
    c_end = N

    k = 0
    while True:
        # 들어갈 숫자가 N의 제곱이 되면 끝
        if k >= N**2:
            break

        for i in range(c_start, c_end):
            k += 1
            snail[r_start][i] = k

        r_start += 1

        for j in range(r_start, r_end):
            k += 1
            snail[j][c_end-1] = k

        c_end -= 1

        for m in range(c_end-1, c_start-1, -1):
            k += 1
            snail[r_end-1][m] = k

        r_end -= 1

        for l in range(r_end-1, r_start-1, -1):
            k += 1
            snail[l][c_start] = k

        c_start += 1

    print('#{} '.format(tc))
    for s in snail:
        print(*s)
