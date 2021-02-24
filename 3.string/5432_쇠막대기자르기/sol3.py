# 스택으로 풀기
import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    arr = list(input())
    # 레이저
    laser = ['(', ')']
    # 막대기 스택
    stack = []
    # 총 조각
    total = 0
    for idx in range(len(arr)):
        # 여는 조각이면 스택
        if arr[idx] == laser[0]:
            stack.append(arr[idx])

        # 닫는 조각이면
        else:
            stack.pop(-1)
            # 닫는 조각이면 레이저인지 검사
            if arr[idx-1] == laser[0]:
                # 레이저면 쌓여있는 막대기만큼 조각 생김
                total += len(stack)
            else:
                # 막대기가 끝나면 끝조각 1개 더 생김
                total += 1




    
    print("#{} {}".format(tc, total))

