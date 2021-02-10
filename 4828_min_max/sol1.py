# min, max, sort없이 풀기
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# max - min

for tc in range(1, T+1):
    t = int(input())
    numbers = list(map(int, input().split()))

    max = numbers[0]
    min = numbers[0]
    for num in numbers:
        if num > max:
            max = num

        if num < min:
            min = num
    result = max - min

    print("#{} {}".format(tc, result))

