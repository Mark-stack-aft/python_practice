dic = {}

while True:
    func = input('기능을 선택하세요 (1 : 삭제, 2 : 추가, 3 : 수정, 0 : 종료) : ')

    if func == '0':
        break

    elif func == '1':
        key = input('삭제할 단어를 입력하세요 : ')

        if key in dic:
            dic.pop(key)

        else:
            print('오류! 삭제할 단어가 없습니다!')

    elif func == '2':
        key = input('추가할 단어를 입력하세요 : ')
        value = input('뜻 : ')
        
        dic[key] = value

    elif func == '3':
        key = input('수정할 단어를 입력하세요 : ')

        if key in dic:
            value = input('수정할 단어의 수정된 뜻을 입력하세요 : ')

            dic[key] = value

        else:
            print('오류! 수정할 단어가 없습니다!')

    else:
        print('잘못 입력하셨습니다.')

    print('현재 사전 :', dic)