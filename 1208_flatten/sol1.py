import sys
sys.stdin = open("input.txt")

# 가로 길이 100, 상자높이 0~100, 덤프횟수 0~1000

def bubblesort(boxs):
    for i in range(len(boxs)-1, 0, -1):
        for j in range(0, i):
            if boxs[j] > boxs[j+1]:
                boxs[j], boxs[j+1] = boxs[j+1], boxs[j]
    return boxs

for tc in range(1, 11):
    dump = int(input())
    boxs = list(map(int, input().split()))

    # dump 횟수가 다 떨어질 때까지
    while dump > 0:
        # 매번 가장 큰 box, 가장 작은 box 다시 정렬
        boxs = bubblesort(boxs)

        # 덤프 횟수 내에 평탄화 완료
        if boxs[-1] - boxs[0] <= 1:
            break

        # dump 1회 감소
        dump -= 1
        # 가장 큰 box에서 가장 작은 box로 옮김
        boxs[0] += 1
        boxs[-1] -= 1


    boxs = bubblesort(boxs)
    result = boxs[-1] - boxs[0]


    print("#{} {}".format(tc, result))

