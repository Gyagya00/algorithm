import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

# {}, ()가 짝을 이뤘는지 검사
# 짝을 이루면 1, 아니면 0
# print('{')는 주어지지 않는다

for tc in range(1, T+1):
    # 확인할 문자열
    check_str = input()
    # print(check_str)

    # stack
    stack = []
    # 짝을 이뤘는지
    res = 1

    for x in check_str:
        # 여는 괄호를 push
        if x == '(' or x == '{':
            stack.append(x)
        # )의 짝이 (인지 확인
        if x == ')':
            # 남은 stack이 없을때
            if not len(stack):
                res = 0
                break
            else:
                y = stack.pop()
                if y != '(':
                    res = 0
                    break
        # }도 확인
        if x == '}':
            if not len(stack):
                res = 0
                break
            else:
                y = stack.pop()
                if y != '{':
                    res = 0
                    break

    # stack이 남아있으면 짝이 안 맞은 것
    if stack:
        res = 0




    print("#{} {}".format(tc, res))

