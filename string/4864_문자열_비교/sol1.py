import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# str1이 str2에 속하는지 확인
# 리스트로 변환해서 str1의 첫 문자가 있는지 체크
# 있다면 str1의 길이만큼 분리해서 같은지 비교

for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    # print(str1, str2)

    # N : str1의 길이 5~100, M : str2의 길이 10~1000
    N = len(str1)
    M = len(str2)

    # 문자열이 있는지 없는지 결과
    res = 0

    # 첫 문자가 str2에 없다면
    if str1[0] not in str2:
        res = 0

    # 첫 문자가 있다면
    for j in range(M):
        if str1[0] == str2[j]:
            # str2의 str1의 첫번째 문자와 일치하는 문자부터 M개만큼 slicing
            # 그리고 str1과 같은지 확인
            if j+N <= M and str2[j:j+N] == str1:
                res = 1
                break
            else:
                res = 0


    print("#{} {}".format(tc, res))

