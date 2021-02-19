import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 문제 짜증나
# 쇠막대기를 자른다 레이저로
# 레이저 : (), 쇠막대기 :(           )
# 몇 개의 조각으로 잘라지는지

# 방법
# ()   (((   ()   ()   ) (   ()   )   ()   )) (   ()   )
#       3            -1  1    -1       -2 1      -1
# 쇠막대기를 기준으로 위에 떨어지는 레이저 개수 세기
#
# 쇠막대기 시작의 개수와 닫기의 개수로 몇번째 쇠막대기인지 알아낸다
# 그 쇠막대기 위에 몇개의 레이저가 닿는지 센다


for tc in range(1, T+1):
    arr = list(input())
    # 레이저
    laser = ['(', ')']


    # 괴상한 레이저 막대기를 숫자로 바꿔줌
    for idx in range(len(arr)):
        # 막대기와 레이저 둘 다 '('이 마지막에 나올 수 없어서
        # 인덱스 에러 없음
        if laser[0] == arr[idx] and laser[1] == arr[idx+1]:
            # 레이저는 1/2로 바꾼다
            arr[idx] = 1/2
            arr[idx+1] = 1/2
        # 막대기 여는 곳 1
        elif laser[0] == arr[idx]:
            arr[idx] = 1
        # 막대기 닫는 곳 -1
        elif laser[1] == arr[idx]:
            arr[idx] = -1

        # arr = [0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, -1, 1, 0.5, 0.5, -1, 0.5, 0.5, -1, -1, 1, 0.5, 0.5, -1]
        #                    3개의 막대기가  2 조각 더 획득

    # 조각의 개수
    pieces = 0
    # 쇠막대기 변화 개수
    steel_h = 0
    # 쇠막대기 총 개수
    steel_total = 0
    for idx in range(len(arr)):
        if arr[idx] == 1:
            steel_total += arr[idx]
    # 레이저 개수
    laser_cnt = 0
    for idx in range(len(arr)):
        # 레이저가 아닐때 막대기가 시작되거나 끝나면
        if arr[idx] != 0.5:
            # 쇠막대기 개수를 구한다
            steel_h += arr[idx]
        # 레이저를 만났을 때
        if arr[idx] == 0.5:
            laser_cnt += arr[idx]
            # 옆에 레이저가 없을 때 막대기 개수가 바뀔때
            if arr[idx+1] != 0.5:
                pieces += steel_h * laser_cnt
                laser_cnt = 0

    pieces += steel_total

    # 레이저개수 * 막대기 개수 + 막대기의 총 개수


    print("#{} {}".format(tc, int(pieces)))

