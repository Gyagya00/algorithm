import sys
sys.stdin = open("input.txt")

T = int(input())

# 농장의 크기는 항상 홀수이다.
# 수확은 농장의 크기에 맞는 정사각형 마름모 형태로
# 수확구역의 숫자를 다 합하는 것
# 수확 구역의 인덱스의 규칙을 알아내자

# 인덱스의 규칙
# 맨 가운데는 항상 수확구역 m//2
# 수확구역은 각 행의 행 인덱스 * 2만큼 더해준다


for tc in range(1, T+1):
    # N N 농장의 크기
    N = int(input())
    # 농장 내 농작물의 가치
    farm = [list(map(int, input())) for _ in range(N)]
    # print(farm)

    for

    print("#{} ".format(tc, ))

