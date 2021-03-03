import sys
sys.stdin = open("input.txt")

T = 10

# 우선순위를 고려해야한다
# 아..... 기억이 안난다..

for tc in range(1, T+1):
    #  N 표기식의 길이
    N = int(input())
    # 중위표기식
    string = input()
    # print(string)

    # 1. 연산자 우선순위 만들어주기
    # stack으로 쌓을 때 우선순위
    in_coming = {'(': 0, '*': 2, '+': 1}
    # stack 내에서의 우선순위
    in_stack = {'(': 3, '*': 2, '+': 1}

    # 2. 후기 표기식으로 바꾼다
    stack = []


    # 3. 후기 표기식을 계산한다
    print("#{} ".format(tc, ))

