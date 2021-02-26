import sys
sys.stdin = open("input.txt")

T = int(input())

# 붕어빵 자격을 얻은 사람 N명
# 0 ~ M초 동안 K개의 붕어빵을 만들 수 있다
# 기다리는 시간없이 붕어빵을 제공할 수 있는지

# 틀린이유
# 1. possible 소문자로...
# 2. 손님이 한꺼번에 올때?
# 3. 0초를 무시함
# 4. 1개 틀림.............. 아으르아르알아ㅡㄹ으앙
# if fish >= N - guest_idx:  # N - guest_idx -1 로 해서 틀림....
#     break


for tc in range(1, T+1):
    # 붕어빵 자격을 얻은 사람 N명
    # 0 ~ M초 동안 K개의 붕어빵을 만들 수 있다
    N, M, K = map(int, input().split())
    # 각 사람이 언제 도착하는지
    guests = list(map(int, input().split()))
    # print(N, M, K)

    # 시간 순서대로 와라 손님
    guests.sort()

    # print(guests)

    # 붕어빵의 개수
    fish = 0
    # 초
    sec = 0
    # 몇번 째 손님이 오는지
    guest_idx = 0
    # 결과
    res = 'Possible'

    while True:
        # 시간이 M만큼씩 흐를 때마다
        if sec != 0 and sec % M == 0:
            # 붕어빵이 K개씩 생긴다.
            fish += K

        # 만약에 붕어빵이 남은 손님 수보다 많거나 같으면 끝
        if fish >= N - guest_idx:  # N - guest_idx -1 로 해서 틀림....
            break

        # 손님이 올 시간이 되면
        while guest_idx < N and guests[guest_idx] == sec:
            # 손님이 붕어빵을 가져간다
            fish -= 1
            # 다음 손님차례
            guest_idx += 1

            # 만약에 붕어빵이 없었으면
            if fish < 0:
                # 미션 실패
                res = 'Impossible'
                break

        sec += 1


    print("#{} {}".format(tc, res))

