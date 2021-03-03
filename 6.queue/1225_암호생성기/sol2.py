# deque
import sys
sys.stdin = open("input.txt")

from collections import deque
# appendleft() pop() append() popleft() extend() extendleft()
T = 10

for _ in range(1, T+1):
    tc = int(input())
    # 빈 큐 만들기
    # deque1 = deque()
    # 원소가 있는 큐 만들기
    de_que = deque(list(map(int, input().split())))

    num = 1
    while True:
        # 첫번째 숫자를 꺼내고
        first = de_que.popleft()
        # num만큼 뺀다
        first -= num

        num += 1

        # 5까지만 num 증가
        if num == 6:
            num = 1

        # 숫자가 0보다 작아지면 0으로 처리
        if first < 1:
            first = 0
            de_que.append(0)
            break

        # 맨 뒤로
        de_que.append(first)

    print("#{} {}".format(tc, ' '.join(list(map(str, de_que)))))

