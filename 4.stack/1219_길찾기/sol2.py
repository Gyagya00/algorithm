import sys
sys.stdin = open("input.txt")

T = 10


for _ in range(1, T+1):
    tc, E = list(map(int, input().split()))
    # print(tc, E) 리스트를 한 거랑 안 한 거랑 차이가 뭐지?

    edge_input = list(map(int, input().split()))
    # 인접행렬
    edge_matrix = [[0 for _ in range(100)] for _ in range(100)]

    # 그래프 => 2차원 리스트로 표현
    for i in range(E):
        start_node, end_node = edge_input[2*i], edge_input[2*i+1]

        edge_matrix[start_node][end_node] = 1

    visited = [False] * 100
    stack = [0]

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True
            # now와 연결된 모든 노드 확인
            for v in range(100):
                if edge_matrix[now][v] and not visited[v]:
                    stack.append(v)

    result = 1 if visited[99] else 0
    
    print("#{} {}".format(tc, result))

