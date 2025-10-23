#그냥 해보고 싶었습니다...

level = '수수수우우미미양양가가가가가가가가가가가'

while True:
    score = int(input('성적을 입력하세요 : '))

    if 4 >= score >= 0: score = 5

    if 100 >= score >= 1:
        print(level[-1 * (score // 5)])


    go = input('계속하시겠습니까?(중단 : q, 계속 : y) : ')

    if go == 'q': break
    elif go == 'y': continue
    else:
        print('잘못 입력 하셨습니다.')
        print(1 / 0)    #일부러 만든 오류


#생각하게 된 과정...

####################

# 100 ~ 90 = -5
# 89 ~ 80 = -4
# 79 ~ 70 = -3
# 69 ~ 60 = -2
# 59 ~ 0 = -1

# for i in range(100, -1, -1):
#     print(i // 5, end = ' ')

#     if i % 10 == 0:
#         print()