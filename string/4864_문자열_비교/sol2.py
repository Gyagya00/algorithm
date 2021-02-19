import sys
sys.stdin = open("input.txt")

def brout_force1(p, t):
    # for 문
    for i in range(len(t)-len(p)+1):
        # 패턴의 길이만큼 반복
        for j in range(len(p)):
            # i : 비교 맨 앞 인덱스, j: 매턴의 길이만큼 비교
            if p[j] != t[i+j]:
                break
        else:
            return 1
    return 0


def brout_force2(p, t):
    i = 0 # t텍스트를 컨트롤 하는 인덱스
    j = 0 # p패턴을 컨트롤 하는 인덱스

    # j가 패턴의 길이가 된다면 찾았다면 멈춘다
    # i가 텍스트의 길이가 된다면 멈춘다.

    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j # i는 j만큼 이동한 상태에서 틀렸기 때문에 시작위치로 돌아가고
            j = -1

        i += 1 # i 옆으로 한칸 이동한다
        j += 1
    if j == len(p): return 1
    else: return 0


T = int(input())
for tc in range(1, T+1):
    
    print("#{} ".format(tc, ))

