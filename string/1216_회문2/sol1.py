import sys
sys.stdin = open("input.txt")

T = 10

# 가장 긴 회문의 길이구하기 100 * 100 행렬
# 직선 경로만 가능
# 회문 1과 다른 점 : 회문의 길이 제한이 없어서 어쩌지?

def trans(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

def pali(matrix, N, M):
    for i in range(N):
        # j + M의 인덱스가 N을 넘지 않게 하기
        for j in range(N-M+1):
            check = matrix[i][j:j+M]
            # M의 길이만큼 잘라서 회문인지 확인
            if check == check[::-1]:
                    return len(check)
    return 0


for tc in range(1, T+1):
    n = int(input())
    # 100 100 글자판
    letters = []
    for _ in range(100):
        letters.append(list(input()))
    # print(letters)

    # 회문의 최대길이
    max_len = 0

    for c in range(100):
        if pali(letters, 100, c) > max_len:
            max_len = pali(letters, 100, c)

    trans(letters)

    for c in range(100):
        if pali(letters, 100, c) > max_len:
            max_len = pali(letters, 100, c)

    
    print("#{} {}".format(tc, max_len))

