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
            i = i-j+1
            j = 0

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

    N = len(A)
    M = len(B)

    # 인덱스
    i, j = 0, 0
    # 중복 되는 문자열 개수
    cnt = 0
    while i < N:
        # 일치하면 계속 쭉쭉쭉 비교
        if B[j] == A[i]:
            j += 1
            i += 1
            # 끝까지 해당 문자열을 비교했을 때
            if j == M - 1:
                cnt += 1
                j = 0
        # 일치하지 않았을 때
        else:
            # i는 j만큼 이동하기 전으로 간 뒤(원래 자리) 거기에서 1만큼 이동
            i = i - j + 1
            # j는 시작부터 다시 비교
            j = 0


    
    print("#{} {}".format(tc, N - M * cnt + cnt))

