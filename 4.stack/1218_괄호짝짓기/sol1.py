import sys
sys.stdin = open("input (1).txt")

T = 10

# 괄호의 짝이 맞는지... 괄호종류가 늘어났네?
# 틀린 이유 여는 괄호 일때 break를 안해줌

for tc in range(1, T+1):
    # N 문자열의 길이
    N = int(input())
    # string 문자열
    string = input()
    # print(N, string)
    # 괄호 종류
    types = [['(', ')'], ['[', ']'], ['{', '}'], ['<', '>']]
    # 유효성
    res = 1

    # 여는 괄호를 저장
    stack = []
    for x in string:
        # 여는 괄호일 때
        for s in types:
            if x == s[0]:
                stack.append(x)
                break

        # 닫는 괄호일 때
        else:
            # stack이 없으면 짝이 안 맞는 것
            if not stack:
                res = 0
                break

            else:
                y = stack.pop()
                for s in types:
                    # 닫는괄호에 맞는
                    if x == s[1]:
                        # 여는 괄호가 아닐때
                        if y != s[0]:
                            res = 0
                            break
                if res == 0:
                    break

    # 다 끝났을 때 남은 괄호가 있다면
    if stack:
        res = 0

    print("#{} {}".format(tc, res))

