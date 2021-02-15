import sys
sys.stdin = open("input.txt")

T = int(input())

# a열과 b열중 더 작은 숫자열에 0을 추가해서 숫자열의 크기를 맞춘다
# 더 작은 숫자열에 앞, 뒤에 넣어가면서
# 곱은 어떻게 하지?
# 같은 idx를 가진 숫자끼리 곱해서 더한다!
# 가장 큰 걸 찾아야지 max 알고리즘


for tc in range(1, T+1):
    # 숫자열 크기
    N, M = map(int, input().split())
    # 숫자열
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 최댓값
    max_sum = 0

    # a, b 숫자열 중 더 작은 숫자열
    c = []
    # a, b 숫자열 중 더 큰 숫자열
    d = []
    # a, b 숫자열 크기 차이 변수
    D = 0

    # a
    if N > M:
        c = b
        d = a
        D = N-M

    else:
        c = a
        d = b
        D = M-N

    # 숫자열 크기만큼 0 더해주기
    for i in range(D+1):
        c_new = [0] * i + c + [0] * (D-i)
        # 곱해서 더해줄 변수
        mul_sum = 0
        for idx in range(len(d)):
            # 인덱스가 같은 것까지 곱한다
            mul_sum += c_new[idx] * d[idx]

        # 가장 큰 것 찾기
        if mul_sum > max_sum:
            max_sum = mul_sum


    print("#{} {}".format(tc, max_sum))

