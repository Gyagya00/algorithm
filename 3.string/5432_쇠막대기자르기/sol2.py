import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    iron_bar = input()

    cnt = 0 # 현재 막대 수
    ans = 0 # 정답

    for i in range(len(iron_bar)):
        # 열린 괄호 막대 추가
        if iron_bar[i] == '(':
            cnt += 1
        else:
            # 닫힌 괄호라면 막대감소
            # 레이저라면 당연히 잘못 세었으니까 빼야지
            # 아니면 어짜피 철봉 끝이니까 빼는 게 맞다
            cnt -= 1

            # 레이저다!
            if iron_bar[i-1] == '(':
                # 레이저로 인해서 잘린 막대들이 생겼으므로
                ans += cnt

            else:
                # 막대 끝이라는 뜻
                # 끝나는 막대조각
                ans += 1

    print("#{} {}".format(tc, ans))


################################################################
T = int(input())

for tc in range(1, T+1):

    iron_bar = input()

    # 실제로 철봉이 담긴 리스트
    s = []
    ans = 0

    for i in range(len(iron_bar)):
        # 열린 괄호라면 s 리스트에 넣기
        if iron_bar[i] == '(':
            s.append('(')
        else:
            # 무조건 꺼내기
            s.pop()

            # 레이저
            if iron_bar[i-1] == '(':
                ans += len(s)
            else:
                ans += 1
