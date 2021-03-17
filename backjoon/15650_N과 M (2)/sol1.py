N, M = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.


stack = []
def perm_order():
    global stack
    if len(stack) == M:
        print(*stack)
        return

    # 스택에 값이 있다면
    if stack:
        for i in range(stack[-1]+1, N+1):
            if i not in stack:
                stack.append(i)
                perm_order()
                stack.pop()

    # 첫 스택값은
    else:
        for i in range(1, N-M+2):
            stack.append(i)
            perm_order()
            stack.pop()

perm_order()

# 숏코딩
# import itertools as I
# N,M=map(int,input().split())
# for i in I.combinations(range(1,N+1),M):print(*i)


# n, m = map(int, input().split())
# arr = [0] * m
# def comb(index, cnt):
#     if cnt == m:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(index, n):
#         arr[cnt] = i + 1
#         comb(i + 1, cnt + 1)
# comb(0, 0)