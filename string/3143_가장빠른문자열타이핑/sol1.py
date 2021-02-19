import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

# A 문자열을 완성하기 위해 눌러야하는 타이핑 최소화
# B이 A에 몇번 들어있는지를 찾아야지
# 앗 틀린이유
# aaaaa aa

for tc in range(1, T+1):
    # A: 타이핑할 문자열 B: A에 속한 문자열
    A, B = map(str, input().split())
    A = list(A)
    B = list(B)
    # print(A, B)


    # 문자열 비교를 위해서 길이
    N = len(A)
    M = len(B)

    # B가 A에 몇번 속하는지 세기
    cnt = 0

    i = 0
    while True:
        if B[0] == A[i] and B == A[i:i+M]:
            cnt += 1
            # 검사한 M개수만큼 이동한다
            i = i + M
        else:
            # 그 옆으로 이동해서 검사
            i += 1
        # i가 인덱스 에러 안나도록!
        if i > N-M:
            break

    # print(cnt)

    # 타이핑 해야 할 횟수
    # N - M * cnt + cnt


    print("#{} {}".format(tc, N - M * cnt + cnt))

