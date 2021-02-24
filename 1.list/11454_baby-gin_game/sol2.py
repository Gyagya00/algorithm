import sys
sys.stdin = open("input.txt")

T = int(input())

def check_babygin(numbers):
    # counter = [0 for _ in range(10)]
    counter = [0] * 10

    is_babygin = 0

    # 카드가 몇 장인지 체크
    for number in numbers:
        counter[number] += 1

    # for idx in range(len(counter)):
    idx = 0
    while idx < len(counter):
        # triplet check
        if counter[idx] >= 3:
            # 카드 세장 버리기
            counter[idx] -= 3
            # 베이비진에 한걸음 다가가기
            is_babygin += 1
            continue

        # run check 카드가 있는지 확인
        if idx < 8:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                # 연속되는 카드 세장 하나씩 버리기
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                # 베이비진에 한걸음 다가가기
                is_babygin += 1
                continue

        # 중간 계산 중에 베이비진이 등장했다면
        if is_babygin == 2:
            return 1
        idx += 1
    # 전부 돌 때까지 베이비진이 없다면
    if is_babygin != 2:
        return 0



for tc in range(1, T+1):
    numbers = list(map(int, input()))
    result = check_babygin(numbers)
    print("#{} {}".format(tc, result))

