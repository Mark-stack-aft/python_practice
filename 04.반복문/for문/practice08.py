print('=' * 50)
print('※섭씨 화씨')
print('=' * 50)

for c in range(-20, 31, 5):
    f = c * 9 / 5 + 32
    print('%5d %6.1f' % (c, f))

print('=' * 50)