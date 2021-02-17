import sys
sys.stdin = open("input (1).txt")

T = int(input())

# 교환 중복 가능
# 가장 큰 금액 찾기

# 풀이
# 가장 큰 숫자(같으면 그 중에서 뒤에 있는 애)가 맨 앞으로 가게 교환
# 맨 앞 고정, 그 뒤부터 cnt만큼 반복
# 교환횟수 소진 전에 가장 큰 숫자가 완성되면 맨 끝 숫자끼리 바꾸기

for tc in range(1, T+1):
    # nums: 숫자판, cnt: 교환횟수
    nums, cnt = map(int, input().split())
    cnt = int(cnt)
    # 각 숫자를 int로 list에 넣는다
    num_list = list(map(int, nums))
    # 비교 시작 인덱스
    k = 0

    while True:
        # 교환횟수가 소진되면 끝
        if cnt == 0:
            break

        # 교환이 cnt 다 쓰기 전에 완료됐을 때
        # 자기 자신과 자리바꾸기 제외
        if k == len(num_list) - 1:
            for i in range(len(num_list)):
                for j in range(len(num_list)):
                    # 같은 숫자끼리 바꾸기
                    if num_list[i] == num_list[j] and i != j:
                        cnt = 0
                        continue
            # 없으면 맨 끝끼리 바꾸기
            else:
                if cnt % 2:
                    num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
                    break
                else:
                    break

        # 최대 num값 찾기
        num = 0
        idx = k

        # k 인덱스부터 끝까지 이동
        for i in range(k, len(num_list)):
            # 같다면 더 뒤에 있는 애를 고르기 위해서 =
            if num_list[i] >= num:
                num = num_list[i]
                idx = i



        # 이미 맨 앞이 최대이면 다음꺼 교환
        if num_list[k] == num_list[idx]:
            k += 1
            continue

        # 맨 앞이랑 자리 바꾸기
        num_list[k], num_list[idx] = num_list[idx], num_list[k]

        # 교환횟수 -1
        cnt -= 1

        # 오른쪽으로 이동
        k += 1


    print("#{} {}".format(tc, ''.join(map(str,num_list))))