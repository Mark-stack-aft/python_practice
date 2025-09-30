first_hour = int(input('첫 번째 시간의 시를 입력하세요 : '))
first_min = int(input('첫 번째 시간의 분를 입력하세요 : '))
second_hour = int(input('두 번째 시간의 시를 입력하세요 : '))
second_min = int(input('두 번째 시간의 분를 입력하세요 : '))

if first_hour == 0: first_hour = 24
if second_hour == 0: second_hour = 24

if 0 <= first_hour <= 24 and 0 <= second_hour <= 24 and 0 <= first_min <= 60 and 0 <= second_min <= 60:

    if first_hour * 60 + first_min < second_hour * 60 + second_min:
        print(f'-빠른 시간 : {first_hour}:{first_min}')
        print(f'-늦은 시간 : {second_hour}:{second_min}')

    elif first_hour * 60 + first_min > second_hour * 60 + second_min:
        print(f'-빠른 시간 : {second_hour}:{second_min}')
        print(f'-늦은 시간 : {first_hour}:{first_min}')

    else:
        print(f'{first_hour}:{first_min}와 {second_hour}:{second_min}의 시간이 같다.')

else:
    print('시와 분이 범위를(시 : 0 ~ 24 (0 = 24), 분 : 0 ~ 60) 벗어났습니다.')