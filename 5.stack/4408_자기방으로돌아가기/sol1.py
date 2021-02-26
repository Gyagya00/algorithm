import sys
sys.stdin = open("input.txt")

T = int(input())

# 몇 단위시간 만에 모든 학생들이 이동할 수 있는지
# 1 -> 4 이동할 때 1 ~ 4 이 현재방이거나 돌아가야할 방이면 같이 이동 불가

# 틀린 이유
# 1. 1번학생과 방을 같이 갈 수 없는 경우를 다 따로 보내서
# 2. 방 경로를 업데이트 안해줌...
# 3. 복도 모양을 보고 예외처리!!

for tc in range(1, T+1):
    # N 학생들의 수
    N = int(input())
    # rooms 현재 방 돌아가야할 방 번호 정보
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # print(rooms)

    # 단위시간 = 한꺼번에 이동할 수 있는 학생들 고려해서
    hours = 0

    # 이동한 학생 체크하기
    student_check = [0 for _ in range(N)]

    # 방번호로 경로를 주는 함수
    def room_num(x):
        # 방 경로 저장
        start_room = min(x)
        end_room = max(x) + 1
        # 작은 방 번호가 짝수이면
        if not min(x) % 2:
            start_room = min(x) - 1
        # 큰 방 번호가 홀수이면
        if max(x) % 2:
            end_room = max(x) + 2
        corridor = [r for r in range(start_room, end_room)]
        return corridor


    for i in range(N-1):
        # 이동 안 한 학생일때
        if not student_check[i]:
            # 이동했다고 표시
            student_check[i] += 1
            # 방 경로 저장
            corridor = []
            corridor.extend(room_num(rooms[i]))



            for j in range(i+1, N):
                # 이동 안 한 학생 중에
                if not student_check[j]:
                    # i번째 학생이랑 방 경로가 겹치는 지 확인
                    if rooms[j][0] not in corridor and rooms[j][1] not in corridor:
                        # 방 경로가 안 겹치면 같이 이동한 걸로
                        student_check[j] += 1
                        # j번째 학생의 방 경로도 추가해주기
                        corridor.extend(room_num(rooms[j]))

            # 경로가 안 겹치는 학생끼리 이동함
            hours += 1

    if not student_check[N-1]:
        hours += 1

    print("#{} {}".format(tc, hours))

