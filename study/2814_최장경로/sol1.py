import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# N개의 정점 1~N, M개의 간선 가중치가 없는 무방향리스트
# 최장경로 계산
# 길이, visited도 같이 stack에 넣을까?

for tc in range(1, T+1):
    # N 정점의 개수 M 간선의 개수
    N, M = map(int, input().split())
    # edge 간선정보
    edges = [list(map(int, input().split())) for _ in range(M)]
    # print(edges)

    # 인접리스트를 만들자
    edge_list = [[] for _ in range(N+1)]
    for edge in edges:
        edge_list[edge[0]].append(edge[1])
        edge_list[edge[1]].append(edge[0])

    # print(edge_list)

    # 방문 스택
    visited_stack = [[0] * (N+1) for _ in range(1, N+1)]

    # 최장 경로 길이
    max_len = 1

    # 경로 스택 + 경로의 길이
    # 시작점이 될 수 있는 모든 정점을 넣는다
    stack = [[x, 1] for x in range(1, N+1)]
    # print(stack)

    while stack:
        # 현재 위치
        v = stack.pop()
        now, length = v
        now_visited = visited_stack.pop()

        # 방문했던 곳인지 확인
        if not now_visited[now]:
            # 방문표시
            now_visited[now] = 1
            # 현재 위치에 연결된 정점 찾기
            for v in edge_list[now]:
                stack.append([v, length+1])
                visited_stack.append(now_visited)

        # 방문했던 곳이면 그 경로는 끝나고 그 전까지 길이를 저장
        else:
            if length-1 > max_len:
                max_len = length-1


    print("#{} {}".format(tc, max_len))

