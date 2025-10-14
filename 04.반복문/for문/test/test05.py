num = input('숫자 입력 : ')

total = 0

for i in num:
    int_num = int(i)

    if int_num % 2 != 0:
        total += 1
 
print('홀수의 개수 : %d 개' % total)