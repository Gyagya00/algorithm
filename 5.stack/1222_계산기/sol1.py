import sys
sys.stdin = open("input (1).txt")

T = 10

# 후위표기식으로 바꿔서 계산하기
# 1. 후위표기식으로 바꾼다
# 연산자는 stack에 담기
# 피연산자는 후위연산자 식에 담기

def add(A, B):
    return A + B

for tc in range(1, T+1):
    # N 문자열 계산식의 길이
    N = int(input())
    # 문자열 계산식
    cal_str = input()
    # print(N, cal_str)

    # 연산자를 담을 곳
    stack = []
    # 후기표기식
    back_cal = []

    for x in cal_str:
        if x == '+':
            if len(stack) > 0:
                # top 확인하기
                y = stack.pop()
                if x == y:
                    back_cal.append(y)
                    stack.append(x)
            else:
                stack.append(x)
        else:
            back_cal.append(x)

    # 나눠서 담은 후에 마지막에 stack에 남은 것이 있다면
    for _ in range(len(stack)):
        back_cal.append(stack.pop())

    # print(back_cal)

    # 후위연산자 식 완성
    # 이제 계산해보자

    # 계산 결과를 담은 stack
    cal_stack = []
    for x in back_cal:
        # 연산자가 아니면 담는다
        if x != '+':
            cal_stack.append(x)
        # 연산자이면 스택에서 피연산자를 두번 pop해서 계산하고 스택에 담는다
        else:
            # 후입선출
            B = int(cal_stack.pop())
            A = int(cal_stack.pop())
            # 계산 결과
            cal_stack.append(add(A, B))
    print("#{} {}".format(tc, cal_stack.pop()))
