import sys
sys.stdin = open("input.txt")

T = 10

# 붙어있는 문자를 소거하기

for tc in range(1, T+1):
    #  N 문자열의 길이 10~100, s 문자열
    N, s = input().split()
    # print(N,s)
    N = int(N)

    # 비교할 문자열 저장
    stack = []

    for x in s:
        # 비교할 문자가 있으면
        if stack:
            # stack에서 꺼낸다
            y = stack.pop()
            # 다르면
            if x != y:
                # stack에 둘 다 저장한다
                stack.append(y)
                stack.append(x)
        # stack이 비면
        else:
            # 넣어주고 다시 비교 시작
            stack.append(x)

    print("#{} {}".format(tc, ''.join(stack)))

