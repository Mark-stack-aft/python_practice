def cm_to_inch(cm):
    inch = cm * 0.393701
    print('%d 센티미터 --> %.2f 인치' % (cm, inch))

def kg_to_pound(kg):
    pound = kg * 2.204623
    print('%d 킬로그램 --> %.2f 파운드' % (kg, pound))

print('- 선택 옵션')
print('''
1. 길이 환산 (센티미터 --> 인치)
2. 무게 환산 (킬로그램 --> 파운드)
''')

option = input('원하는 환산 단위 입력 (1/ 2) : ')

if option == '1':
    cm = int(input('센티미터 단위의 길이를 입력하세요 : '))
    cm_to_inch(cm)

elif option == '2':
    kg = int(input('킬로그램 단위의 길이를 입력하세요 : '))
    kg_to_pound(kg)

else:
    print('잘못 입력하셨습니다.')