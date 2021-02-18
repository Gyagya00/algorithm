import sys

sys.stdin = open("input.txt")

T = int(input())

# 패턴이 반복되는 부분 : 마디의 길이 출력
# 문자를 앞에서부터 []에 담는다
# 문자가 []내에 있는지 확인한다 => 원래 담겨있는 문자면 거기부터 새로운 []에 넣는다
# 새로운 []를 기존 []에 in 되는지 확인한다.
# 아니면 기존 []와 새로운 []를 합친다.

# a = [1, 2]
# b = [1, 2, 3]
# print(a in b) # 흠 a를 하나씩 꺼내서 확인해야겠네


for tc in range(1, T + 1):
    # 패턴들
    pats = list(input())
    # print(pats)

    # 패턴을 담을 리스트
    p = []
    # 패턴을 비교할 리스트
    com_p = []

    for i in range(len(pats)):
        # 문자가 p에 없으면
        if pats[i] not in p:
            # p에 담아준다
            p.append(pats[i])
        # 같은 문자가 p에 있으면
        else:
            # 그 뒤부터 com_p에 담아준다
            for j in range(i, len(pats)):
                com_p.append(pats[j])
                # com_p가 p에 속하는지 계속 확인
                for pp in com_p:
                    # 속하면 같은 패턴이니까 무시
                    if pp in p:
                        continue
                    # 안 속하면 패턴이 아직 안 끝난 거니까
                    # 패턴에 이어 붙여주고
                    # 새로운 비교리스트 만들기
                    else:
                        p.extend(com_p)
                        com_p.clear()
    # print(p)
    print("#{} {}".format(tc, len(p)))


    # # 그 뒤부터 com_p에 담아준다
    # for j in range(i, len(pats)):
    #     com_p.append(pats[j])
    #
    #     # com_p가 p와 같은지 확인
    #     if com_p != p:
    #         # 패턴이 아직 안 끝난 거니까
    #         # p에 com_p의 요소를 이어 붙여주고
    #         # 새로운 비교리스트 만들기
    #         for pp in com_p:
    #             p.append(pp)
    #             com_p.remove(pp)
    #             com_p.append(pats[i+len(p)])
    #             if
    #
    # # 같으면 패턴완성 break!
    # else:
    #     break


