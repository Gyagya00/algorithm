import sys
sys.stdin = open("input.txt")

T = int(input())

# 회문검사...
# 기억이 안나는데 흠

for tc in range(1, T+1):
    # 문자열 리스트
    string = list(input())
    # print(string)

    # 뒤집어보자
    pali = []
    for idx in range(len(string)-1, -1, -1):
        pali.append(string[idx])

    if string == pali:
        res = 1
    else:
        res = 0
    
    print("#{} {}".format(tc, res))

