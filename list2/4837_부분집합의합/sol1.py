import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

# A의 부분 집합 중
# N개의 원소 포함 & 원소의 합이 K인 부분집합의 개수
# 없으면 0

for tc in range(1, T+1):
    N, K = map(int, input().split())

    A = [x for x in range(1, 13)]

    # 전체 부분집합 리스트
    subs = []
    # 전체 부분집합 구하기
    for i in range(1 << 12):
        s = []
        for j in range(12):
            if i & (1 << j):
                s.append(A[j])
        subs.append(s)

    # 조건에 맞는 부분집합 개수
    cnt = 0

    # 조건에 해당하는 부분집합 찾기
    for s in subs:
        n, k = 0, 0
        for x in s:
            # 원소 개수 세기
            n += 1
            # 원소의 합
            k += x
        if n == N and k == K:
            cnt += 1

    print("#{} {}".format(tc, cnt))

