print('-' * 50)
print('%7s %7s %7s' % ('킬로그램', '파운드', '온스'))
print('-' * 50)

for kg in range(100, 201):
    pound = kg * 2.204623
    ounce = kg * 35.273962
    print('%8d %12.1f %11.1f' % (kg, pound, ounce))

print('-' * 50)