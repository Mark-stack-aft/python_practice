print('\n' * 28)
print('-' * 50)
print()
rate = input('등급을 입력해 주세요(A+ ... F) : ')
print()
print('-' * 50)

if rate.upper() == 'A+':
    print()
    print('-' * 50)
    print()
    print('등급 : A+, 평점 : 4.5')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'A':
    print()
    print('-' * 50)
    print()
    print('등급 : A, 평점 : 4.0')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'B+':
    print()
    print('-' * 50)
    print()
    print('등급 : B+, 평점 : 3.5')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'B':
    print()
    print('-' * 50)
    print()
    print('등급 : B, 평점 : 3.0')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'C+':
    print()
    print('-' * 50)
    print()
    print('등급 : C+, 평점 : 2.5')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'C':
    print()
    print('-' * 50)
    print()
    print('등급 : C, 평점 : 2.0')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'D+':
    print()
    print('-' * 50)
    print()
    print('등급 : D+, 평점 : 1.5')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'D':
    print()
    print('-' * 50)
    print()
    print('등급 : D, 평점 : 1.0')
    print()
    print('-' * 50)
    print()

elif rate.upper() == 'F':
    print()
    print('-' * 50)
    print()
    print('등급 : F, 평점 : 0')
    print()
    print('-' * 50)
    print()

else:
    print()
    print('-' * 50)
    print()
    print(f'오류! {rate.upper()} 이(가) (A+ ... F) 에 속하지 않습니다.')
    print()
    print('-' * 50)
    print()