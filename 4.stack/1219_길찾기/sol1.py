import sys
sys.stdin = open("input.txt")

T = 10

# S: 0에서 G: 99까지 갈 수 있는 지
# 최대 2개의 갈림길 일방통행

for tc in range(1, T+1):
    # tcc 테스트케이스 번호, E 길(간선)의 총개수
    tcc, E = map(int, input().split())
    # 간선들 다 받은 리스트
    edges = list(map(int, input().split()))

    # 인접 리스트로 표현해보자
    # 인접리스트 0 ~ 99까지
    edge_list = [[] for _ in range(100)]
    for i in range(E):
        start_node, end_node = edges[2*i], edges[2*i+1]
        edge_list[start_node].append(end_node)
    # print(edge_list)

    # 갈 수 있는 노드 저장
    stack = [0]
    # 방문한 노드 표시
    visited = [0] * 100
    # 결과 길이 있는지
    res = 0

    # 갈 수 있는 노드가 있을 때까지
    while stack:
        # 현재 노드
        now = stack.pop()
        # 방문 안 했을 때
        if not visited[now]:
            # 방문한 것으로 바꾸기
            visited[now] = 1
            # 지금 (now)에서 갈 수 있는 (연결된) 노드 찾기
            for v in edge_list[now]:
                # 갈 수 있는 노드에 저장
                stack.append(v)
        # 목표노드에 도달했을 때
        if visited[99]:
            res = 1
            break


    
    print("#{} {}".format(tc, res))

