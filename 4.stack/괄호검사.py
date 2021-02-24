# def check(P):
#     stack = []
#     for p in P:
#         if p == '(':
#             stack.append(p)
#         else:
#             if len(stack) > 0:
#                 stack.pop(-1)
#             else:
#                 return '( 가 부족합니다.'
#
#     if len(stack) == 0:
#         return '괄호가 잘 매치됩니다.'
#     else:
#         return ') 가 부족합니다.'
#
# print(check('(('))

############################################################

stack = []

input_string = '(((((((((((('
for s in input_string:
    if s == '(':
        stack.append(s)
    else:
        if len(stack) == 0:
            result = False
            break
        stack.pop()

else:
    if len(stack):
        result = False
    else:
        result = True

print(result)