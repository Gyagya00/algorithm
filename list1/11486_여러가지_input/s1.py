import sys
sys.stdin = open('input.txt')

# input으로 들어오는 데이터는 모두 string, 형변환 필요
N = int(input())
result = 1 if N%2 == 1 else 0
print(result)

# '1 2 3 4 5 '를  split()으로 공백 기준 나눔 ['1', '2', '3', '4', '5']
# 각 인자를 map(int, )를 사용해서 int로 바꾼 뒤 다시 제자리에 넣어줌
# 마지막으로 list
numbers = list(map(int, input().split()))
result = sum(numbers)
print(result)

N = int(input())
numbers = []
for i in range(N):
    row = list(map(int,input().split()))
    numbers.append(row)
result = numbers[1][1]
print(result)

