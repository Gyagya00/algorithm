N, M = map(int, input().split())

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

stack = []
def perm_multi(cnt):
    if cnt == M:
        print(*stack)
        return
    for i in range(1, N+1):
        stack.append(i)
        perm_multi(cnt+1)
        stack.pop()

# N, M = 3, 3
perm_multi(0)