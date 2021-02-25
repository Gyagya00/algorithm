import sys
sys.stdin = open("input.txt")

T = 10

# 연산자 개수가 2개이다
# 우선순위를 구분해야해
# 왜 안되는지 모르겠다...

for tc in range(1, T+1):
    # N 테스트케이스의 길이
    N = input()
    # 계산식
    cal = input()
    # print(N, cal)

    # 딕셔너리는 어려워 써보자
    cal_type = {'+': 0, '*': 1}

    # 1. 후위표기식으로 바꾸자

    # 후기표기식용 연산자 스택
    stack = []
    # 후기표기식을 담을 리스트
    post_fix = []

    for x in cal:
        # 연산자이면
        if x == '*' or x == '+':
            # 연산자 스택이 비어있다면
            if not stack:
                stack.append(x)

            else:
                # 연산자 top보다 x가 더 크다면 (우선 순위가 높다면)
                if cal_type[x] > cal_type[stack[-1]]:
                    # 쌓기
                    stack.append(x)
                # top이랑 같거나 작다면

                # 우선순위가 더 낮다면
                else:
                    while cal_type[x] <= cal_type[stack[-1]]:
                        # 연산자 스택의 top
                        y = stack.pop()
                        # top은 후위표기식으로
                        post_fix.append(y)
                        # 스택이 비면 끝
                        if not stack:
                            break
                    # 다 끝났을 때 x는 stack으로
                    stack.append(x)
        # 그냥 숫자라면
        else:
            post_fix.append(x)

    # 남은 stack은 post_fix에 담아준다
    post_fix.extend(stack)
    print(post_fix)

    # 2. 이제 후위계산식을 계산해야해.. 이런

    # 계산 결과를 담을 스택
    res_stack = []
    for x in post_fix:
        if x == '+':
            B = int(res_stack.pop())
            A = int(res_stack.pop())
            res_stack.append(A+B)
        elif x == '*':
            B = int(res_stack.pop())
            A = int(res_stack.pop())
            res_stack.append(A*B)
        else:
            res_stack.append(x)

        # print(res_stack)


    print("#{} {}".format(tc, res_stack[-1]))

