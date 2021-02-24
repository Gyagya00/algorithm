import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 반복문자를 지운 후 남은 문자열의 길이 출력
# 남은 문자열 없으면 0
# 문자열의 요소는 지울 수가 없으니까 리스트로 받자

for tc in range(1, T+1):
    # 반복문자를 포함한 문자열 s
    s = input()
    # print(s)

    # 이전문자 저장
    stack = []

    for x in s:
        # stack에 요소가 있으면
        if len(stack):
            y = stack.pop()
            # 직전이랑 다르면
            if y != x:
                # 둘 다 스택에 저장
                stack.append(y)
                stack.append(x)
        # stack이 비었으면
        else:
            # 넣어주고 다시 시작
            stack.append(x)
    
    print("#{} {}".format(tc, len(stack)))

