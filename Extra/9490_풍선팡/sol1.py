import sys
sys.stdin = open("input1.txt")

T = int(input())

# 풍선이 M개씩 N개의 줄에
# 어떤 풍선을 터트리면 꽃가루개수만큼 상하좌우로 풍선이 더 터진다
# 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합의 최대값

for tc in range(1, T+1):
    # N행, M열
    N, M = map(int, input().split())
    # flower 꽃가루의 개수가 적힌 행렬
    flower = [list(map(int, input().split())) for _ in range(N)]

    # 델타
    # 상 하 우 좌
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    flower_sum = 0
    for i in range(N):
        for j in range(M):
            
    
    print("#{} ".format(tc, ))

