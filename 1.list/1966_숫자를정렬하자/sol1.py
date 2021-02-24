import sys
sys.stdin = open("input (1).txt")

T = int(input())

def bubblesort(num):
    for i in range(len(num)-1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

for tc in range(1, T+1):
    # N개의 숫자
    N = int(input())
    num = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')

    print(' '.join(map(str, bubblesort(num))))

