import sys
sys.stdin = open("input.txt")

T = int(input())

# 수열 만드는 함수
# n은 input list, k는 생성된 수열
# def perm(n, k = []):
#     if len(k)
#         return k
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 return perm(n[i+1:], k.append(n[i]))


for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    for a in range(len(numbers)):
        for b in range(len(numbers)):
            if a != b:
                for c in range(len(numbers)):
                    if a != c and b != c:
                        for d in range(len(numbers)):
                            if a != d and b != d and c != d:
                                for e in range(len(numbers)):
                                    if a != e and b != e and c != e and d != e:
                                        for f in range(len(numbers)):
                                            if a != f and b != f and c != f and d != f and e != f:
                                                perm = [numbers[a], numbers[b], numbers[c], numbers[d], numbers[e], numbers[f]]

                                                if numbers[a] == numbers[b] == numbers[c]

    # print("#{} ".format(tc, ))

