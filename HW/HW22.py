def add(num1, num2):
    print('%d + %d = %d' % (num1, num2, num1 + num2))

def minus(num1, num2):
    print('%d - %d = %d' % (num1, num2, num1 - num2))

def multiply(num1, num2):
    print('%d x %d = %d' % (num1, num2, num1 * num2))

def divide(num1, num2):
    print('%d ÷ %d = %.1f' % (num1, num2, num1 / num2))

print('- 선택 옵션')
print('''
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
''')

option = input('원하는 연산을 입력하세요 (1 / 2 / 3 / 4) : ')

if option == '1' or option == '2' or option == '3' or option == '4':
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))

    if option == '1':
        add(num1, num2)

    elif option == '2':
        minus(num1, num2)

    elif option == '3':
        multiply(num1, num2)

    elif option == '4':
        divide(num1, num2)

else:
    print('잘못 입력하셨습니다.')