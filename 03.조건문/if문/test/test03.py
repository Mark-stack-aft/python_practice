print('\n' * 28)
print('-' * 50)
print()
spend = int(input('구매 금액 : '))
print()
print('-' * 50)
print()

if 10000 <= spend < 50000:
    rate = 5.0

elif 50000 <= spend < 300000:
    rate = 7.5

elif 300000 <= spend:
    rate = 10.0

else:
    rate = 0

discount = spend * rate / 100
pay = spend - discount

print('-' * 50)
print()
print(f'구매 금액 : {spend}')
print()
print('-' * 50)
print()
print(f'할인율 : {rate:.1f}')
print()
print('-' * 50)
print()
print(f'할인 금액 : {discount:.0f}')
print()
print('-' * 50)
print()
print(f'지불 금액 : {pay:.0f}')
print()
print('-' * 50)