print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print('-' * 50)
print()
print('아르바이트 급여 계산 프로그램')
print()
print('-' * 50)
print()
print('※ 시급')
print('-주간 근무 : 9,500원')
print('-야간 근무 : 주간 시급 * 1.5')
print()
print('-' * 50)
print()

hour_pay = 9500

question = int(input('1(주간근무) 또는 2(야간근무)을 입력해주세요 : '))
print()
print('-' * 50)
print()
work_time = int(input('근무 시간을 입력해주세요 : '))
print()
print('-' * 50)
print()

if question == 1:
    day_night = '주간'
    pay = hour_pay * work_time

elif question == 2:
    day_night = '야간'
    pay = hour_pay * work_time * 1.5

print('%d시간 동안 일한 %s 급여는 %d원 입니다.' %(work_time, day_night, pay))
print()
print('-' * 50)