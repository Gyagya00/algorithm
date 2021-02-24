import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

# 가장큰 가장작 2큰 2작 ...
# 정렬을 하고 그중에서 뽑아쓰기?

def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a


for tc in range(1, T+1):
    # N : 정수의 개수
    N = int(input())
    # 정렬할 숫자들
    nums = list(map(int, input().split()))

    # 오름차순
    nums = bubble_sort(nums)

    # 특별한 정렬
    res = [0] * len(nums)

    # 뽑아올 인덱스
    left = 0
    right = len(nums) - 1

    for idx in range(0, len(res), 2):
        # 홀수 개일 때 인덱스 에러 방지
        if idx == len(res) - 1:
            res[idx] = nums[left]
            break
        else:
            # 작은 거 넣기
            res[idx] = nums[right]
            # 큰 거 넣기
            res[idx + 1] = nums[left]
            # 인덱스 이동
            left += 1
            right -= 1

            # 인덱스가 같아지면 끝
            if left == right:
                break




    print("#{} {}".format(tc, ' '.join(map(str, res[0:10]))))

