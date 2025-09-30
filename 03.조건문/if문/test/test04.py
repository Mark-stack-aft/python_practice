userid = input('아이디 : ')

if userid == 'admin':
    print('콘텐츠 이용이 가능합니다!')

else:
    level = int(input('회원 레벨 (1 ~ 9) : '))

    if 1 <= level <= 3:
        print('콘텐츠 이용이 가능합니다!')

    else:
        print('콘텐츠를 이용할 수 없습니다!')