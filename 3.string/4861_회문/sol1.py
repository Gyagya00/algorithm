import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 회문을 찾아라 가로 세로 둘다
# 리스트를 왼 오, 오 왼 두개 만들어서 (상하 하상) 전치행렬 만들기
# 하나를 뒤집으면서 같은지 확인

# 전치행렬 만들기
def trans(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix






# trans는 원래 행렬을 바꾸는 함수다
# k = [[x for x in range(10)] for _ in range(10)]
# print(k)
# print(trans(k), trans(k))

def pali(matrix, N, M):
    for i in range(N):
        # j + M의 인덱스가 N을 넘지 않게 하기
        for j in range(N-M+1):
            check = matrix[i][j:j+M]
            # M의 길이만큼 잘라서 회문인지 확인
            if check == check[::-1]:
                    return check
    return 0


for tc in range(1, T+1):
    # N * N 글자판 M: 회문의 글자수
    N, M = map(int, input().split())
    # 글자판
    letters = []
    for _ in range(N):
        letters.append(list(input()))

    # 회문 저장소
    res = []

    res = pali(letters, N, M)

    if not res:
        res = pali(trans(letters), N, M)

    # print(res)

    print("#{} {}".format(tc, ''.join(res)))

