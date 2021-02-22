# len(letters[i]) > j의 조건으로 하면 문자열 길이를 맞춰줄 필요없다
# print(letters[i][j], end = '')으로 하면 str을 만들어줄 필요없다
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 의석이 글자 개수가 다른데
# 빈공간을 어떻게 채울까?
# 가장 큰 문자의 길이를 기준으로 그보다 작은 구역에 ~과 같은 문자를 넣고
# 그 문자가 나오면 넘어가면서 append?

for tc in range(1, T+1):
    # 문자열의 길이가 1~15
    # 문자열 모음 행렬
    letters = [list(input()) for _ in range(5)]
    # print(letters)

    # 가장 긴 문자열 찾기
    max_len = 0
    for x in letters:
        if len(x) > max_len:
            max_len = len(x)

    # 문자열 길이 맞춰주기
    for x in letters:
        while len(x) < max_len:
            x.append('*')

    # 열 방향으로 탐색
    # 빈 스트링
    str = ''
    for j in range(max_len):
        for i in range(5):
            # len(letters[i]) > j
            if letters[i][j] != '*':
                str += letters[i][j]


    # print(letters)
    print("#{} {}".format(tc, str))

