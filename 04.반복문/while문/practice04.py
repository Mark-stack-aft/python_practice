print('f를 입력하면 종료')
s = input('알파벳을 입력하세요 : ')

if s == 'f':
    print('종료')

else:
    print('f가 아님')

print('-' * 50)

while True:
    s = input('알파벳 입력 : ')

    if s != 'f':
        print(f'입력하신 알파벳은 "{s}"입니다.')

    else:
        print('입력하신 알파벳이 f이므로 종료합니다.')
        break