import sys
sys.stdin = open("input (1).txt")

T = 10

# 교착상태의 개수 구하기
# 교착상태 기준이 뭘까? 위 아래 순서로 붙어있는 빨 파 결합 개수
#   1, 위: N극     2, 아래: S극

# 풀이방법
# 일단 열탐색으로 해야돼
# 열탐색으로 1, 2 순서의 배열 세기?

for tc in range(1, T+1):
    # N 테이블 한 변의 길이
    N = int(input())
    # 자성체가 놓인 테이블
    table = [list(map(int, input().split())) for _ in range(N)]
    # print(table)


    cnt = 0

    for j in range(N):
        stack = []
        for i in range(N):
            if table[i][j] == 1:
                # stack이 비어있을 때만
                if not stack:
                    stack.append(1)

            elif table[i][j] == 2:
                # 스택에 1이 있다면
                if stack:
                    stack.pop()
                    cnt += 1


    print("#{} {}".format(tc, cnt))

