# BFS DFS에서 pop() -> pop(0)
import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

# stack에는 내가 갈 수 있는 노드를 저장
# pop을 했을 때 비로소 내가 방문함


for tc in range(1, T+1):
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)
    V, E = map(int, input().split())

    # 인접 배열
    edge_matrix = [[0] * (V+1) for _ in range(V+1)]
    # print(edge_matrix)
    for _ in range(E):
        start_node, end_node = list(map(int, input().split()))
        edge_matrix[start_node][end_node] = 1

    # S 시작노드, G 목표노드
    S, G = map(int, input().split())
    # print(edge_matrix, S, G)

    # 방문여부 체크리스트
    visited = [0] * (V+1)
    # 방문할 수 있는 노드 리스트
    queue = [S]
    # 목표노드에 도달했는지
    res = 0

    while queue:
        # 현재 노드
        now = queue.pop(0)
        # 방문한 적없는 노드라면 (방문한 노드면 아무 조치 없이 넘어감)
        if not visited[now]:
            # 방문체크해주자
            visited[now] = 1
            # 연결된 노드 확인
            for j in range(V+1):
                # 방문확인빼먹음
                if edge_matrix[now][j]:
                    queue.append(j)
        # 목표노드에 갔다면
        if visited[G]:
            res = 1
            break


    print('#{} {}'.format(tc, res))


