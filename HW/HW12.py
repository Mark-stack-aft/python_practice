print('-' * 50)
print('%7s %7s %7s %7s' % ('cm', 'mm', 'm', 'inch'))
print('-' * 50)

for cm in range(1, 51):
    mm = cm * 10.0
    m = cm * 0.01
    inch = cm * 0.3937
    print('%7d %7d %7.2f %7.2f' % (cm, mm, m, inch))

print('-' * 50)