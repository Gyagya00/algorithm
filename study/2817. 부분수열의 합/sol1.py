import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 합이 K가 되는 경우의 수를 구하자
# 모든 부분집합을 구해서 더해야 겠나?
# 어휴 기억도 안나는데 큰일이야

# 틀린이유가 뭐지?
# j의 범위를 왜때문에 4로 했어ㅠㅜㅠ N이잖아

for tc in range(1, T+1):
    # N 자연수의 개수 1~20, K 목표 합 1~1000
    N, K = map(int, input().split())
    # A : N개의 자연수가 있는 리스트, 자연수 1~100
    A = list(map(int, input().split()))
    # print(N, K, A)

    # 경우의 수
    cnt = 0

    for i in range(1, 1 << N):
        # 부분집합
        sub = []
        for j in range(N):
            if i & (1 << j):
                sub.append(A[j])
        # print(sub)

        # sum 많이했다
        if sum(sub) == K:
            # print(sub)
            cnt += 1



    print("#{} {}".format(tc, cnt))

