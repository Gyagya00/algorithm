# 브루트 포스로 해보자!
import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

def brout_cnt(A, B, N, M):
    # i: A 인덱스 j: B 인덱스
    i, j = 0, 0
    cnt = 0
    while i < N-M and j < M:
        if B[j] == A[i]:
            j += 1
            i += 1

        else:
            i = i-j
            j = -1

        if j == M-1:
            cnt += 1

        if i == N-M-1:
            return cnt





for tc in range(1, T+1):
    # A: 타이핑할 문자열 B: A에 속한 문자열
    A, B = map(str, input().split())
    A = list(A)
    B = list(B)
    # print(A, B)

    # 문자열 비교를 위해서 길이
    N = len(A)
    M = len(B)


    
    print("#{} {}".format(tc, N - M*brout_cnt(A, B, N, M) + brout_cnt(A, B, N, M)))

