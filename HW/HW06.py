rate = input('등급을 입력해 주세요(A+ ... F) : ')

if rate.upper() == 'A+':
    avg = 4.5

elif rate.upper() == 'A':
    avg = 4.0

elif rate.upper() == 'B+':
    avg = 3.5

elif rate.upper() == 'B':
    avg = 3.0

elif rate.upper() == 'C+':
    avg = 2.5

elif rate.upper() == 'C':
    avg = 2.0

elif rate.upper() == 'D+':
    avg = 1.5

elif rate.upper() == 'D':
    avg = 1.0

elif rate.upper() == 'F':
    avg = 0

else:
    avg = -4.5

if avg == -4.5:
    print(f'오류! {rate.upper()} 이(가) (A+ ... F) 에 속하지 않습니다.')
    
else:
    print(f'등급 : {rate.upper()}, 평점 : {avg}')