import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    building_count = int(input())
    building_list = list(map(int, input().split()))

    # 조망권이 확보된 집
    total = 0

    for i in range(building_count):
        # 현재위치
        now = building_list[i]

        # 현재위치에 건물이 없다면 다음 건물로 이동
        if now == 0:
            continue

        else:
            # 최대높이 저장용
            max_height = 0
            # 좌우 두개씩 총 네번 반복
            for j in range(4):
                # 나를 제외한 건물 중에 가장 큰 건물 고르기
                if building_list[i+idx[j]] > max_height:
                    idx = [-2, -1, 1, 2]
                    max_height = building_list[i+idx[j]]

        # 내가 나머지 네개보다 크다면
        if now > max_height:
            # 차이만큼 조망권 확보
            total += now - max_height


    print("#{} {}".format(tc, total))

