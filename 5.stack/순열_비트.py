arr = [1, 2, 3]

N = 3

sel = [0] * N # 뽑은 결과를 적음

# check 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return
    for i in range(N):
        # i번째 원소를 활용했는지 체크! 활용했으면 쓰면 안돼!
        if check & (1<<i): continue

        sel[idx] = arr[i]
        perm(idx+1, check | (1<<i)) # 원상복구가 필요없다 합집합으로 임시로 활용한 것 표시

perm(0, 0)