import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    my_len = 0
    my_sum = 0
    for number in numbers:
        my_len += 1
        my_sum += number

    result = round(my_sum / my_len)
    print('#{} {}'.format(tc, result))
