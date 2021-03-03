import sys
sys.stdin = open("input.txt")

T = int(input())

# 분할정복문제이다

for tc in range(1, T+1):
    # N 인원수
    N = int(input())
    # N명이 고른 카드
    cards = list(map(int, input().split()))
    # print(cards)

    def winner(cards, idx = N):
        if len(cards) == 1:
            return cards[0]
        if len(cards) == 2:
            if cards[0] == cards[1]:
                return cards[0]
            elif cards[0] == 1:
                if cards[1] == 2:
                    return cards[1]
                if cards[1] == 3:
                    return cards[0]
            elif cards[0] == 2:
                if cards[1] == 1:
                    return cards[0]
                if cards[1] == 3:
                    return cards[1]
            else:
                if cards[1] == 1:
                    return cards[1]
                if cards[1] == 2:
                    return cards[0]

        half_winner1 = winner(cards[:(1+len(cards)) // 2 + 1], idx = (1+len(cards)) // 2 + 1)
        half_winner2 = winner(cards[(1+len(cards))//2 + 1:], idx = len(cards))

        return winner(list(half_winner1, half_winner2))

    print("#{} ".format(tc, ))

