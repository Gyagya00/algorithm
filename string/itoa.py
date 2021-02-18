# 숫자를 문자로 바꾸는 함수
def itoa(num):
    str = '{}'.format(num)
    return str

num = 10
print(itoa(num), type(itoa(num)))

# ord를 사용하여 아스키 코드 값으로 변환
def itoa2(my_int):
    my_str = []

    while my_int != 0:
        r = my_int % 10
        my_int //= 10

        # 숫자도 str 상태로 아스키 코드에 할당되어 있대!
        num = chr(ord('0') + r)  # ord('0') : 48 + 3 => 51 => chr(51) => '3'
        my_str.append(num)

    my_str.reverse()
    return ''.join(my_str)

print(itoa2(123), type(itoa2(123)))