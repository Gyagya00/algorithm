import sys
sys.stdin = open("input.txt")

T = int(input())

# 원재야 제발 정신차려
# 0100의 3번째 비트를 1로 바꾸면 0111
# 초기화 상대 (00000..) 가 원래 상태로 돌아가는 최소 몇번 고치면 될까
# 뒤에는 계속 바뀌니까 앞부터 하나씩 바꾸면 되겠지..?


for tc in range(1, T+1):
    # 비트 원래값을 리스트로
    bit = list(map(int, input()))
    # print(bit)
    # 비트 초기값
    bit_0 = [0] * len(bit)

    # 최소 수정 횟수
    cnt = 0

    # 하나씩 비교할 거야
    for i in range(len(bit)):
        if bit_0[i] != bit[i]:
            cnt += 1
            for j in range(i, len(bit)):
                bit_0[j] = bit[i]


    print("#{} {}".format(tc, cnt))

