import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N 개의 숫자, M번 맨앞의 숫자를 맨 뒤로
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # print(numbers)

    for _ in range(M):
        first = numbers.pop(0)
        numbers.append(first)

    print("#{} {}".format(tc, numbers.pop(0)))

