import sys

sys.stdin = open("input (1).txt")

# 높은 숫자를 앞으로 배치하는 함수
# 파라미터: 교환횟수, 카운트, 큰 거 앞으로 빼고 난 뒤의 첫번째 인덱스, 입력 숫자(숫자 리스트형태)
# 궁극적으로 교환해야하는 횟수와 카운트가 같아질 때까지 반복
def cal(chan, cnt, k, nums_c):
    # 교환횟수가 0이 되었을 때
    if chan == cnt:
        str_num = list(map(str, nums_c))
        int_num = int("".join(str_num))
        # 전역변수 maxx 사용 선언
        global maxx
        # maxx와 마지막 배치 숫자를 비교
        if maxx < int_num:
            maxx = int_num
        # print(int_num)
        return
    else:
        # k=0부터 넣어주면 첫번째 인덱스 부터
        piv = nums_c[k]
        # 첫번째 인자를 제외한 리스트
        temp = nums_c[k + 1:]
        val = max(temp)
        # 가장 큰 수가 앞에 없을 때
        if val > piv:
            for i in range(len(temp)):
                if temp[i] == val:
                    # 새로운 배열을 만들기 위해 얕은 복사
                    cop = nums_c[:]
                    # 맨 앞의 수와 가장 큰 수 교환
                    cop[k], cop[i + k + 1] = cop[i + k + 1], cop[k]
                    # 맨앞자리 제외하고 복사된 리스트로 cal 함수 반복
                    cal(chan, cnt + 1, k + 1, cop)
        # 가장 큰 수가 맨 앞에 있을 때
        else:
            # 큰 수를 앞으로 보내는 정렬이 진행되면서 k가 마지막에서 두번째 인덱스에 도착했을 때
            if k == len(nums_c) - 2:
                # 숫자 중복이 있을 때 그 둘을 교환하면 똑같기 때문에 cnt => chan 수정하고 cal 함수 시행해서 종료시켜버리기
                if len(set(nums_c)) < len(nums_c):
                    cal(chan, chan, k + 1, nums_c)
                    return
                # 숫자 중복이 없을 때
                else:
                    # 남은 교환 횟수가 짝수일때
                    if (chan - cnt) % 2 == 0:
                        # 어떤 두수 교환을 짝수번 반복하면 똑같기 때문에 cnt => chan 수정하고 cal 함수 시행해서 종료시켜버리기
                        cal(chan, chan, k + 1, nums_c)
                        return
                    # 남은 교환 횟수가 홀수일때
                    else:
                        # 차선책을 선택하기 위해 맨 뒤의 두자리만 바꿔주고 cnt => chan 수정하고 cal 함수 시행해서 종료시켜버리기
                        nums_c[-1], nums_c[-2] = nums_c[-2], nums_c[-1]
                        # 맨 앞자리 제외하고 cal 함수 반복
                        cal(chan, chan, k + 1, nums_c)
                        return
            # 맨 앞자리 제외하고 cal 함수 반복
            # 가장 큰게 맨 앞에 있으므로 교환은 이뤄지지 않았으니 cnt 증가 x
            else:
                cal(chan, cnt, k + 1, nums_c)


T = int(input())

for tc in range(1, T+1):
    nums, chan = map(int, input().split())
    # 숫자로 이루어진 리스트 형태로 변환
    nums = list(map(int, str(nums)))

    # 교환을 시행하는 카운트
    cnt = 0
    # 최대상금 0으로 초기화
    maxx = 0

    cal(chan, cnt, 0, nums)
    
    # 결과 출력
    print("#{} {}".format(tc, maxx))