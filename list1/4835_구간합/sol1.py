import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# N개의 정수
# 이웃한 M개의 합 : 가장 큰 경우, 작은 경우의 차이

# 문제를 잘 읽자 멍충멍충
# 정렬해서 하는 건 줄 알았자나아아아아
# def bubblesort(n):
#     for i in range(len(n)-1, 0, -1):
#         for j in range(0, i):
#             if n[j] > n[j+1]:
#                 n[j], n[j+1] = n[j+1], n[j]
#     return n


for tc in range(1, T+1):
    n, m = map(int, input().split())
    ai_list = list(map(int, input().split()))

    # 초기 max min 설정하기
    max_ai = 0
    min_ai = 0
    for ai in ai_list[0: m]:
        max_ai += ai
        min_ai += ai


    for idx in range(len(ai_list)):
        # for i in range(len(numbers) - M + 1): 으로 하면 index 걱정 끝!!
        # 혹시 index가 넘어갈까봐
        if m+idx-1 < len(ai_list):
            # sum은 매번 바껴서 비교해야되니까 여기서 초기화
            sum_ai = 0
            # m개씩 더해주기
            for ai in ai_list[idx : m+idx]:
                sum_ai += ai

            if sum_ai > max_ai:
                max_ai = sum_ai

            if sum_ai < min_ai:
                min_ai = sum_ai

    result = max_ai - min_ai

    print("#{} {}".format(tc, result))

