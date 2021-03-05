# 4871_그래프경로
# DFS 재귀로 풀어보자
import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T+1):
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)
    V, E = map(int, input().split())

    # 인접행렬
    matrix = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        start_node, end_node = map(int, input().split())
        matrix[start_node][end_node] = 1
        matrix[end_node][start_node] = 1

    # 출발노드 S 도착노드 G
    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    res = 0

    # DFS재귀
    def dfs(S, G):
        # global할 필요없음 리스트내의 리스트참조시에는
        global visited, res
        now = S

        if now == G:
            for x in visited:
                if x:
                   res = 1
            return res

        # 방문한 적없는 노드
        if not visited[now]:
            visited[now] = 1
            # 연결된 노드들에 대해서 DFS
            for v in range(V+1):
                if not visited[v] and matrix[now][v]:
                    dfs(v, G)

    dfs(S, G)

    print("#{} {}".format(tc, res))

