import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# N개의 정점, M개의 간선 가중치가 없는 무방향리스트
# 최장경로 계산

for tc in range(1, T+1):
    # N 정점의 개수 M 간선의 개수
    N, M = map(int, input().split())
    # edge 간선정보
    edges = [list(map(int, input().split())) for _ in range(M)]
    # print(edge)

    # 인접리스트를 만들자
    edge_list = [[] for _ in range(N+1)]
    for edge in edges:
        edge_list[edge[0]] += edge[1]
        edge_list[edge[1]] += edge[0]

    print(edge_list)
    print("#{} ".format(tc, ))

