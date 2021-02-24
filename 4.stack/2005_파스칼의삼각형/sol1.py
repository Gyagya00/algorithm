import sys
sys.stdin = open("input.txt")

T = int(input())

# 파스칼의 삼각형
# 리스트? 행렬? 어떻게 표현할 수 있을까?
# 인덱스 규칙보기

for tc in range(1, T+1):
    # N 파스칼 삼각형의 크기
    N = int(input())

    # 파스칼 삼각형
    pas = [[1] * x for x in range(1, N+1)]

    for i in range(1, N-1):
        # (pas[1] 리스트의 길이 - 1)만큼 보기
        for j in range(len(pas[i])-1):
            # pas[2] = 1 2 1 에서 2 (2, 1)는 1(1, 0) 1(1, 1)을 더한 것이다.
            pas[i+1][j+1] = pas[i][j] + pas[i][j+1]


    print("#{}".format(tc))
    for p in pas:
        print(*p)

