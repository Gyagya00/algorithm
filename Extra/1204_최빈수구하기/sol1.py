import sys
sys.stdin = open("input.txt")

T = int(input())

# 카운트 정렬

for tc in range(1, T+1):
    t = input()
    scores = list(map(int, input().split()))

    # 카운트 정렬
    cnts = [0] * 100

    for x in scores:
        for idx in range(100):
            if idx == x:
                cnts[idx] += 1
    # print(cnts)
    for idx in range(100):
        if max(cnts) == cnts[idx]:
            max_num = idx
    
    print("#{} {}".format(tc, max_num))

