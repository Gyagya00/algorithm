# 반복문을 이용한 거듭제곱 O(n)

def iterative_power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# 분할정복을 이용한 거듭제곱 O(logn)

def recursive_power(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        y = recursive_power(x, n//2)
        return y * y
    else:
        y = recursive_power(x, (n-1)//2)
        return y * y * x

print(iterative_power(2, 1000))
print(recursive_power(2, 1000))
