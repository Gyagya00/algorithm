T = int(input())

for tc in range(1, T+1):
    # N * N 배열, M * M 파리채
    N, M = map(int, input().split())
    flies = []

    for i in range(N):
        flies.append(list(map(int, input().split())))

    max_dead = 0
    # 행, 열 시작값
    i, j = 0, 0

    while i < N-M+1:
        # 파리채 한 번으로 죽은 파리 값을 저장할 임시 변수
        temp_flies = 0
        
        # 시작값인 i,j부터 파리채 만큼의 범위에 해당하는 M까지 더한 값이 최종값
        for k in range(i, i + M):
            for l in range(j, j + M):
                temp_flies += flies[k][l]

        # 한 칸씩 옆으로 가기 위해 j += 1
        j += 1
		
        # 범위의 끝까지 왔다면 한 칸 아래로 내려가고 j는 0이 된다.
        if j == (N-M+1):
            i += 1
            j = 0

        # 현재 죽은 파리가 최고치를 경신하면 그 값을 최고값으로 저장
        if temp_flies > max_dead:
            max_dead = temp_flies

    print("#{} {}".format(tc, max_dead))