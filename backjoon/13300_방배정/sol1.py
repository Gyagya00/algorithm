import sys
sys.stdin = open("input.txt")

T = 2

# 학년이 같고 성별이 같으면 한방에 담을 수 있다.
# 학년, 성별 그룹 만큼 방을 만들고 K개를 초과하는 수만큼 방을 더 만들면된다


for tc in range(1, T+1):
    # N, K : 수학여행에 참가하는 학생수, 한 방에 배정할 수 있는 최대인원
    N, K = map(int, input().split())
    # 학생 [성별01, 학년1~6]
    students = [list(map(int, input().split())) for _ in range(N)]
    # print(N, K, students)

    # 카운트 리스트
    cnt_list = [0] * 12

    # 방의 수
    rooms = 0

    # 카운트 리스트 만들기
    for i in range(len(students)):
        # 여학생이면 카운트리스트의 0~5 인덱스에서 숫자를 세준다
        if students[i][0] == 0:
            cnt_list[students[i][1]-1] += 1
        # 남학생이면 카운트리스트의 6~12 인덱스에서 숫자를 세준다
        else:
            cnt_list[students[i][1]+5] += 1

    # 학생수와 K를 비교
    for idx in range(12):
        # 학생이 있으면
        if cnt_list[idx] > 0:
            # 방을 만들고
            rooms +=1
            # 학생이 K명보다 많으면
            if cnt_list[idx] > K:
                # K랑 같거나 작아질 때까지 방 만들고 학생 배정하고 반복
                while cnt_list[idx] > K:
                    cnt_list[idx] -= K
                    rooms += 1
        else:
            continue

    print(rooms)

