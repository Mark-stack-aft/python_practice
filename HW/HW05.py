print('\n' * 28)
print('-' * 50)
print()
num = int(input('수를 입력하세요 : '))
print()
print('-' * 50)

if num in range(0, 1000):
    if len(str(num)) == 3:
        length = '세'

    elif len(str(num)) == 2:
        length = '두'

    elif len(str(num)) == 1:
        length = '한'
        
    print()
    print('-' * 50)
    print()
    print(f'{num} 은(는) {length} 자리 숫자이다.')
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