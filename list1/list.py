a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# * : 언팩 연산자
# 리스트 밖으로 나옴
# print(*a)
#
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         print(a[i][j])


b = [1, 2, 3, 4]

# 부분집합의 총 개수 : 0000 0001 0010 ...
for i in range(1 << len(b)):
    # j는 0, 1, 2, 3 => b에 접근할 인덱스
    for j in range(len(b)):
        # (1 << j) 하나하나 요소 : 0001 0010 0100 1000
        # 각 부분집합에 어떤 요소가 들어있는지 확인
        # i : 0011 & 0001(1) 0010(2) 0100(3) 1000(4)와 전부 비교 => 0001(1), 0010(2)
        if i & (1 << j):
            print(b[j], end='')
    print()