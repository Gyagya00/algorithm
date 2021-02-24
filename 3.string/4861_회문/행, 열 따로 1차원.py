matrix = []  # 가로방향으로 문자들을 가지고 와서 리스트에 저장
colmatrix = []  # 세로방향으로 문자들을 가지고 와서 리스트에 저장
for i in range(N):
    matrix.append(input())
# print(matrix)
for i in range(N):
    colstring = ''
    for j in range(N):
        colstring += matrix[j][i]
    colmatrix.append(colstring)
# print(colmatrix)