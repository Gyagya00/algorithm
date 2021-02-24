import sys
sys.stdin = open("input.txt")

T = 1


for tc in range(1, T+1):
    binggo = []
    for i in range(5):
        binggo += list(map(int, input().split()))
    ans = []
    for i in range(5):
        ans += list(map(int, input().split()))
    cnt = 0
    sum_low = [0 for i in range(5)]
    sum_col = [0 for i in range(5)]
    sum_dia = [0 for i in range(2)]

    for i in range(25):
        idx = binggo.index(ans[i])
        binggo[idx] = 0
        for j in range(5):
            if sum(binggo[5 * j:5 * j + 5]) == 0:
                sum_low[j] = 1
            if sum(binggo[j:j + 21:5]) == 0:
                sum_col[j] = 1
        if sum(binggo[0:26:6]) == 0:
            sum_dia[0] = 1
        if sum(binggo[4:21:4]) == 0:
            sum_dia[1] = 1
        if sum(sum_low) + sum(sum_col) + sum(sum_dia) >= 3:
            iter = i + 1
            break
    print(iter)

