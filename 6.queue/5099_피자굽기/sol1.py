import sys
sys.stdin = open("input.txt")

T = int(input())

# 틀린 이유
# 피자 전체가 한꺼번에 화덕에 들어갈 수 없을 수 있음 N != M

for tc in range(1, T+1):
    # N 화덕의 크기 M 피자 개수
    N, M = map(int, input().split())
    # 치즈의 양
    cheese = list(map(int, input().split()))
    # print(cheese)

    # [치즈번호, 치즈양] 큐 만들기
    pizza = []
    for idx in range(M):
        pizza.append([idx+1, cheese[idx]])

    oven = pizza[:N]
    pizza = pizza[N:]
    # print(oven, pizza)

    while len(oven) > 1:
        # 1번 위치의 피자
        out = oven.pop(0)

        # 치즈가 다 안 녹으면
        if out[1] != 0:
            out[1] //= 2
            oven.append(out)

        # 치즈가 다 녹으면 다음 피자를 넣어줌
        else:
            if pizza:
                new_pizza = pizza.pop(0)
                new_pizza[1] //= 2
                oven.append(new_pizza)

    print("#{} {}".format(tc, oven[0][0]))

