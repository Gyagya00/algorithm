# N = int(input())

# 1번부터 N번까지 카드
# 1번 제일 위, N번 제일 아래
# 1. 제일 위에 버리고
# 2. 그 다음 제일 위 카드 제일 아래로
# 한 장 남을 때까지

for N in range(1, 10):
    cards = []
    for i in range(1, N+1):
        cards.append(i)

    # 한 장 남을 때까지
    while len(cards) > 1:
        # 1. 제일 위 버린다
        cards.pop(0)
        # 2. 제일 위 아래로
        cards.append(cards.pop(0))

    print(*cards)

# ########################################################

# 시간 초과
# 그림 그려야지

last_cards = [1,]
i = 2
n = 1
while True:
    last_cards.append(i)
    if i == 2**n:
        i = 2
        n +=1
        continue
    
    i +=2 
    if len(last_cards) == 6:
        break


print(last_cards[-1])

##############################################
N = int(input())

from collections import deque

queue = deque()
for i in range(1, N+1):
    queue.append(i)
    
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(*queue)

