import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 부족한 카드의 장수 알아내기
# 중복된 카드가 있으면 ERROR

for tc in range(1, T+1):
    # 갖고 있는 카드 정보
    cards = list(input())
    # print(cards)

    # 카드하나씩 분리한 리스트
    s_cards = []
    for idx in range(0, len(cards), 3):
        # 카드별로 구분하기
        if cards[idx:idx+3] not in s_cards:
            s_cards.append(cards[idx:idx+3])

    # 카드 종류
    # 중복카드 확인
    if len(cards)//3 != len(s_cards):
        res = 'ERROR'
        print('#{} {}'.format(tc, res))
    else:
        res = [13, 13, 13, 13]
        for i in range(len(s_cards)):
            if s_cards[i][0] == 'S':
                res[0] -= 1
            elif s_cards[i][0] == 'D':
                res[1] -= 1
            elif s_cards[i][0] == 'H':
                res[2] -= 1
            else:
                res[3] -= 1

        print('#{}'.format(tc), end=' ')
        for i in res:
            print(i, end=' ')
        print()

