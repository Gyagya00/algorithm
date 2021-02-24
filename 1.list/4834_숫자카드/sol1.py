import sys
sys.stdin = open("sample_input.txt")
T = int(input())

# N : 카드 장수
# ai : N개의 숫자가 여백없이
# 가장 많은 카드의 숫자, 장 수
# 단! 카드 장수가 같으면 적힌 숫자가 큰 쪽을 출력

# 풀이
# 숫자를 하나씩 뜯어낸다.
# 각각의 카드 개수를 센다 countsort?
# 값이 같으면 큰 거 출력

# 숫자를 하나씩 뜯어냄
def splitt(n):
    sp_list = []
    while n > 10:
        sp_list.append(n%10)
        n = n // 10
    sp_list.append(n)
    return sp_list

# 숫자가 띄어쓰기없이 붙어있을 땐 list(map(int, input())으로 나눌 수 있다구!
# cards =[int(card) for card in input()] 로 바꿀 수 있다.

# countsort
def count_sort(n):
    count = [0] * 10
    for idx in n:
        count[idx] += 1
    return count

for tc in range(1, T+1):
    N = int(input())
    ai_dummy =int(input())

    # 숫자를 하나씩 뜯어서 리스트에 넣는다
    ai_list = splitt(ai_dummy)
    # countsort
    count_list = count_sort(ai_list)

    # 카드 장 수
    max_count = count_list[0]
    # 카드 숫자
    max_idx = 0

    # 다행히 장 수가 같으면 카드 숫자가 큰 게 나오면 됨
    for idx in range(len(count_list)):
        # 카드 장 수가 큰 거
        if count_list[idx] >= max_count:
            max_count = count_list[idx]
            max_idx = idx

    print("#{} {} {}".format(tc, max_idx, max_count))

