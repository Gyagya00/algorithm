# 리스트로
import sys
sys.stdin = open("input.txt")

T = 10

# 1감소 뒤 ~~ 5감소 뒤
# 0보다 작아지는 경우 0으로 유지 => 암호

for _ in range(1, T+1):
    tc = int(input())
    # 8개 숫자
    queue = list(map(int, input().split()))

    num = 1
    while True:
        # 첫번째 숫자를 꺼내고
        first = queue.pop(0)
        # num만큼 뺀다
        first -= num

        num += 1

        # 5까지만 num 증가
        if num == 6:
            num = 1

        # 숫자가 0보다 작아지면 0으로 처리
        if first < 1:
            first = 0
            queue.append(0)
            break

        # 맨 뒤로
        queue.append(first)

    print("#{} {}".format(tc, ' '.join(list(map(str, queue)))))

