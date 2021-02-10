import sys
sys.stdin = open("input.txt")

# 왼쪽일 수록(인덱스가 작을 수록) 숫자가 크다
# 높이가 높을 수록(해당 인덱스의 값이 클 수록) 숫자가 크다
# 계산
# 오른쪽과의 간격 (len - 인덱스) - 나랑 높이가 같거나 큰 상자의 개수 (x >= 나}
T = int(input())

def max_distance(numbers):
    #  최댓값 변수
    max = 0

    # 오른쪽과의 간격
    for i in range(len(numbers)):
        # 혹시 막대가 없을 때가 계산된 건가?
        if numbers[i]:
            gap = len(numbers) - i - 1

            # 나랑 높이가 같거나 큰 상자의 개수
            count = 0
            # 내 오른쪽에 위치한 상자 중에 나랑 높이가 같거나 큰 상자의 개수
            for j in range(i+1, len(numbers)):
                if numbers[j] >= numbers[i]:
                    count += 1

            distance = gap - count
            # 최대 낙차 찾기
            if distance > max:
                max = distance
    # 절대.. 들여쓰기 공부해....
    #         return max => 처음에 max보다 큰 distance가 들어왔을 때 바로 return
    return max


for tc in range(1, T+1):
    # 방의 가로 세로 길이
    N_tc = int(input())
    numbers = list(map(int, input().split()))
    result = max_distance(numbers)
    print("#{} {}".format(tc, result))

import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    
    print("#{} ".format(tc, ))

