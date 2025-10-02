phone_number = input('전화번호 입력 : ')

for i in phone_number:
    if i != '-':
        print(i, end = '')