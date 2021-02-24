import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 카드를 반으로 나누고 교대로 카드를 뽑아서 새로운 덱
# N이 홀수이면 먼저 놓는 쪽에 한 장 더

# 틀린 이유
# 출력은 어려웡

for tc in range(1, T+1):
    # N: 카드의 개수
    N = int(input())
    # N개의 카드 이름
    cards = list(input().split())
    # print(cards)

    # 카드를 나누자
    # 홀수면
    if N % 2:
        # 먼저 놓는 쪽에 하나 더
        cards1 = cards[:N//2 + 1]
        cards2 = cards[N//2 + 1:]
    # 짝수면
    else:
        cards1 = cards[:N // 2]
        cards2 = cards[N // 2:]

    # print(cards1, cards2)

    print("#{}".format(tc), end = ' ')

    # 교대로 놓아보자
    for idx in range(len(cards2)):
        print(cards1[idx], end = ' ')
        print(cards2[idx], end = ' ')
    # 홀수 일때
    if N % 2:
        print(cards1[-1], end = ' ')
    print()

