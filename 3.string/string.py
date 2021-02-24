print(ord('B'))

line = '안녕하세요'

print(line.replace('세', '시'))
print(line) # 원래 line이 나온다

print(line.split('하'))
print(line) # 원래 line
 # 바꿀 수 없다! immutable

print(line.find('녕')) # 없으면 -1
print(line.index('녕')) # 없으면 에러

# == vs is
# 값 비교, 할당된 객체 비교