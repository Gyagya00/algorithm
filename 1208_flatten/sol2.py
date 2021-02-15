import sys
sys.stdin = open("input.txt")

T = int(input())

# 최저 높이의 상자 인덱스 위치반환
def min_search():
    #초기화
    min_value = 987654321
    min_idx = -1

    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i

    return min_idx

def max_search:
    max_value = 0
    max_idx = -1

    for i in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
            max_idx = i
    return max_idx

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))

    # N번 덤프하기
    for i in range(N):
        # 최고 높이 상자 한 칸 내리기
        box[max_search()] -= 1
        # 최저 높이 상자 한 칸 올리기
        box[min_search()] += 1

    
    print("#{} {} {}".format(tc, box[max_search()], box[min_search()]))

####################################################################################
#count_sort

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] * 101

    # 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]


    while N > 0 and min_value < max_value-1:
        # 상자 옮기기
        h_cnt[min_value] -= 1
        h_cnt[min_value+1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value-1] += 1

        # 포인터를 변경하자
        if h_cnt[min_value] == 0:
            min_value += 1

        if h_cnt[max_value] == 0:
            max_value -= 1

        # 덤프줄이기

    print('#{} {}'.format(tc, h_cnt[max_value] -  h_cnt[min_value]))