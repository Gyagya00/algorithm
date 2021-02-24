def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(35))

# 구했던 수도 구해야 해서 불필요한 호출이 많다.
# 중복 호출이 많다! => memoization으로 해결가능

# 메모이제이션
def fibo1(n):
    if n >= 2 and n >= len(memo):
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
print(fibo1(40))


##################################
memo2 = [-1] * 20
memo2[0] = 0
memo2[1] = 1

def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)

    return memo2[n]

print(fibo2(10))