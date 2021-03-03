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




    # # 인접 리스트
    # edge_list = [[] for _ in range(V+1)]
    # for _ in range(E):
    #     start_node, end_node = list(map(int, input().split()))
    #     edge_list[start_node].append(end_node)
    #
    # S, G = list(map(int, input().split()))
    #
    # # 방문여부 체크리스트
    # visited = [False] * (V+1)
    # # 시작위치를 스택에 담기
    # stack = [S]
    #
    # # 스택에 아무것도 없으면 다 확인한 것
    # while stack:
    #     # pop을 통해 현재 위치를 알 수 있다.
    #     now = stack.pop()
    #     # 방문한 경우
    #     if visited[now]:
    #         pass
    #     # 방문하지 않은 경우
    #     else:
    #         visited[now] = True
    #         # 현재 노드(now)와 연결된 모든 노드를 반복
    #         for v in edge_list[now]:
    #             # 방문하지 않은 노드라면
    #             if not visited[v]:
    #                 stack.append(v)
    #
    # result = 1 if visited[G] else 0


    # print("#{} {}".format(tc, result))

