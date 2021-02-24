import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 누가 먼저 쪽 번호를 찾는지
# 이진 탐색...

def page(find, right, cnt = 0, left = 1,):
    if left == find or right == find:
        return cnt
    # 비교할 중간 페이지
    c = int((left + right)/2)
    # 탐색횟수
    cnt += 1
    # 페이지가 시작 ~ 중간 사이에 있으면
    if find > left and find < c:
        right = c
        return page(find, right, cnt, left, )
    else:
        left = c
        return page(find, right, cnt, left, )

for tc in range(1, T+1):
    # 전체 쪽수, a가 찾을 쪽번호, b가 찾을 쪽 번호
    P, a, b = map(int, input().split())

    if page(a, P) > page(b, P):
        winner = 'B'
    elif page(a, P) == page(b, P):
        winner = 0
    else:
        winner = 'A'

    print("#{} {}".format(tc, winner))

