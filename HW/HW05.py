print('\n' * 28)
print('-' * 50)
print()
num = int(input('수를 입력하세요 : '))
print()
print('-' * 50)

if 0 <= num <= 999:
    if len(str(num)) == 3:
        print()
        print('-' * 50)
        print()
        print(f'{num} 은(는) 세 자리 숫자이다.')
        print()
        print('-' * 50)
        print()

    elif len(str(num)) == 2:
        print()
        print('-' * 50)
        print()
        print(f'{num} 은(는) 두 자리 숫자이다.')
        print()
        print('-' * 50)
        print()

    elif len(str(num)) == 1:
        print()
        print('-' * 50)
        print()
        print(f'{num} 은(는) 한 자리 숫자이다.')
        print()
        print('-' * 50)
        print()

else:
    print()
    print('-' * 50)
    print()
    print(f'오류! {num} 은(는) 범위(0~999) 이외의 숫자이다.')
    print()
    print('-' * 50)
    print()