import sys
sys.stdin = open("input.txt")

T = int(input())

# 기억이 안난다!
# 연산자 + - / * 뿐인가?
# 틀린 이유
# 1. 4/2 = 2.0 => int로 변환해줘야 됨
# 2. 예외중에 숫자가 더 많은 경우 고려안함

for tc in range(1, T+1):
    # string 연산코드
    string = input().split()
    # print(string)

    # 연산자
    cal = ['+', '-', '/', '*']

    # 숫자를 담을 스택
    stack = []

    res = 'error'

    for x in string:
        if x == '.':
            if len(stack) != 1: # 틀린이유 #2
                break
            res = int(stack.pop())

        # 숫자면
        elif x not in cal:
            # 스택에 쌓는다
            stack.append(x)

        else:
            # 형식이 잘못돼서 스택에 숫자가 2개보다 적을 때는 에러
            if len(stack) > 1:
                B = int(stack.pop())
                A = int(stack.pop())

                if x == cal[0]:
                    stack.append(A + B)
                elif x == cal[1]:
                    stack.append(A - B)
                elif x == cal[2]:
                    stack.append(A / B)
                else:
                    stack.append(A * B)
            else:
                break

    print("#{} {}".format(tc, res))
