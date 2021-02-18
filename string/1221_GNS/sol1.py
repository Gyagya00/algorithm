# sort를 쓰자!
import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())


for tc in range(1, T+1):
    # N : 문자열의 길이
    t, N = input().split()
    N = int(N)

    # 문자열
    num_str = list(input().split())
    # print(N, num_str)

    # 숫자 사전
    dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}

    # 딕셔너리는 어려워
    for idx in range(len(num_str)):
        for key in dict.keys():
            # 숫자 사전의 key와 일치하면 영어를 해당 숫자로 바꾸기
            if num_str[idx] == key:
                num_str[idx] = dict[key]

    # print(num_str)

    # 숫자로 바꾼 상태에서 정렬
    new_str = sorted(num_str)

    for idx in range(len(new_str)):
        for key in dict.keys():
            # 숫자를 다시 사전의 value와 같으면 해당 영어로 바꾼다
            if new_str[idx] == dict[key]:
                new_str[idx] = key

    # print(new_str)

    print('#{}'.format(tc), end = '\n')
    for s in new_str:
        print(s, end = " ")


