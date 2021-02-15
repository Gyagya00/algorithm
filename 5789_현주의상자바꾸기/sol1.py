import sys
sys.stdin = open("sample_input.txt")

T = int(input())
# N개의 상자
# i(<=Q)번째 작업에 대해서 L번 상자부터 R번 상자까지 값을 i로 변경
# Q회동안 작업, N개의 상자에 적혀있는 값


for tc in range(1, T+1):
    N, Q = map(int, input().split())

    # 초기 상자
    box = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = i

    print("#{} {}".format(tc, ' '.join(map(str, box))))

