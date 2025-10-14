total = 0

for i in range(1, 101):
    if i % 3 == 0:
        total += i

print('1 ~ 100 까지의 3의 배수의 합계 : %d' % total)