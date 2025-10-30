#그냥 해보고 싶었습니다...

level = '수수수우우미미양양가가가가가가가가가가가가'

while True:
    score = int(input('성적을 입력하세요 : '))

    if 100 >= score >= 0: print(level[-1 * ((score // 5) + 1)])

    else: print('범위(100~0)을 벗어났습니다.')


    go = input('계속하시겠습니까?(중단 : q, 계속 : y) : ')

    if go == 'q': break
    elif go == 'y': continue
    else:
        print('잘못 입력 하셨습니다.')
        print(1 / 0)    #일부러 만든 오류