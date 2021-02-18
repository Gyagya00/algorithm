
import sys
sys.stdin = open("input.txt")

T = int(input())

# 패턴이 반복되는 부분 : 마디의 길이 출력
# 방법 1
# 문자를 앞에서부터 []에 담는다
# 문자가 []내에 있는지 확인한다 => 원래 담겨있는 문자면 거기부터 새로운 []에 넣는다
# 새로운 []를 기존 []에 in 되는지 확인한다.
# 아니면 기존 []와 새로운 []를 합친다.

# a = [1, 2]
# b = [1, 2, 3]
# print(a in b) # 흠 a를 하나씩 꺼내서 확인해야겠네

# blackpink가 오답이야 이유가 뭘까 k는 blackpin에 속해있지만 패턴이 끝나지 않았어 p와 com_p의 맨 앞을 비교하자!
# 만약에 klackpink가 패턴이면 대처 못한다
# 다시 짜면 더 잘할 수 있을 거같아

# 방법2
# 새로운 아이디어 in이 아니라 ==로 패턴 자체가 동일한지 확인하자 and com_p를 만들지 말고 슬라이싱을 이용하자


for tc in range(1, T+1):
    # 패턴들
    pats = list(input())
    # print(pats)

    # 패턴을 담을 리스트
    p = []

    # # 패턴을 비교할 리스트
    # com_p = []

    for i in range(len(pats)):
        # 문자가 p에 없으면
        if pats[i] not in p:
            # p에 담아준다
            p.append(pats[i])
        # 같은 문자가 p에 있으면
        else:
            # p와 p 이후의 길이만큼을 떼서 비교
            if p == pats[i:i+len(p)]:
                # 같으면 끝
                break

            # 같지 않으면 p에 더 담아!
            p.append(pats[i])


    print(p)

    print("#{} {}".format(tc, len(p)))
