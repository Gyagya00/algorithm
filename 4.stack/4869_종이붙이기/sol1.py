import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 20 N 직사각형에 20 10 / 20 20 종이를 빈틈없이 붙이기
# N은 10의 배수
# 종이를 붙이는 경우의 수

for tc in range(1, T+1):
    # 20 * N 직사각형, 10의 배수
    N = int(input())
    # N에 따른 경우의 수 리스트
    cases = [0, 1]
    for x in range(2, N//10+1):
        # 10, 30, 50, 70 ...
        if x % 2:
            cases.append(cases[-1]*2 -1)
        else:
            cases.append(cases[-1]*2 +1)



    print("#{} {}".format(tc, cases[-1]))

