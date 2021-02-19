import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

# str1의 글자들이 str2에 몇개 들어있는지 가장 많은 글자 개수 출력
# 그냥 하나씩 세면 되지 않을까?

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # print(str1, str2)

    max_cnt = 0
    for x in str1:
        cnt = 0
        for y in str2:
            if x == y:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt


    print("#{} {}".format(tc, max_cnt))

