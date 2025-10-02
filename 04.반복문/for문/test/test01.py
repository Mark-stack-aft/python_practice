count = 0

for i in range(200, 800):
    if i % 5 != 0:
        print(i, end = ' ')
        count += 1

        if count % 10 == 0:
            print()

print('\n' + '=' * 50 + '\n')
print(f'200부터 800까지의 범위 중 5의 배수가 아닌 수의 개수는 {count}개 입니다.')
print('\n' + '=' * 50 + '\n')