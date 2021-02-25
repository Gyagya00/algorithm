import sys
sys.stdin = open("input.txt")

T = int(input())

# 10개의 평점
# 중간 35 기말 45 과제 20
# 각 평점은 같은 비율로

# 틀린이유가 뭘까
# 1. sort한 상태에서 K번째라니...멍충이야ㅜㅠㅜㅠㅜㅠㅠㅜㅠㅜ
# K번째 친구가 sort하고 어디로 간지 알아야겠다
# 2. 오름차순 정렬을 하다니..
# 왜 이렇게 복잡하게 푼 거같지...?

for tc in range(1, T+1):
    # N 학생수
    # K 학점을 알고 싶은 학생의 번호
    N, K = map(int, input().split())
    # 각 학생이 받은 과제의 점수
    scores = [list(map(int, input().split())) for _ in range(N)]
    # print(scores)

    # 총점을 구하는 공식
    total_score = []
    for i in range(N):
        total_score.append(scores[i][0]*0.35 + scores[i][1]*0.45 + scores[i][2]*0.2)
    # print(total_score)

    # K번째 학생의 점수는?
    K_student = total_score[K-1]
    # print(K_student)

    # 선택정렬
    for i in range(N):
        for j in range(i+1, N):
            if total_score[i] < total_score[j]:
                total_score[i], total_score[j] = total_score[j], total_score[i]

    # print(total_score)
    # 정렬된 상태에서 K번째 학생의 바뀐 인덱스는?
    for idx in range(N):
        if total_score[idx] == K_student:
            K_idx = idx

    # print(K_idx)

    # 평점리스트
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    # 학생들에게 평점을 부여하자
    student_grade = []
    for x in grade:
        for _ in range(N//10):
            student_grade.append(x)

    # print(student_grade)


    print("#{} {}".format(tc, student_grade[K_idx]))

