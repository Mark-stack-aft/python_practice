import random

game = ['가위', '바위', '보']

me_point = 0
computer_point = 0

print('''
------------------------
| 가위 바위 보 게임 시작 |
------------------------
''')

while True:
    me = input('가위, 바위, 보 중 하나를 입력하세요 (종료 : 0) : ')

    computer_index = random.randint(0, 2)

    computer = game[computer_index]

    if me == '0':
        print('''
---------------------
| 게임을 종료합니다. |
---------------------
''')
        
        print()
        print('-' *50)
        print()
        print(f'''
나의 점수     : {me_point}
컴퓨터의 점수 : {computer_point}
''')
        print()
        print('-' *50)
        print()

        print()

        break

    if not me in game:
        print('''
-------------------    
| 다시 입력하세요! |
-------------------
''')
        
        print()
        print('-' *50)
        print()
        print(f'''
나의 점수     : {me_point}
컴퓨터의 점수 : {computer_point}
''')
        print()
        print('-' *50)
        print()

        continue

    if me == computer:
        print('''
---------          
| 무승부 |
---------
''')
        
        print()
        print('-' *50)
        print()
        print(f'''
나의 점수     : {me_point}
컴퓨터의 점수 : {computer_point}
''')
        print()
        print('-' *50)
        print()

    elif me == '가위' and computer == '보':
        print('''
-------------
| 나의 승리! |
-------------
''')
        me_point += 1

        print()
        print('-' *50)
        print()
        print(f'''
나의 점수     : {me_point}
컴퓨터의 점수 : {computer_point}
''')
        print()
        print('-' *50)
        print()

    elif me == '보' and computer == '바위':
        print('''
-------------
| 나의 승리! |
-------------
''')
        me_point += 1

        print()
        print('-' *50)
        print()
        print(f'''
나의 점수     : {me_point}
컴퓨터의 점수 : {computer_point}
''')
        print()
        print('-' *50)
        print()

    elif me == '바위' and computer == '가위':
        print('''
-------------
| 나의 승리! |
-------------
''')
        me_point += 1

        print()
        print('-' *50)
        print()
        print(f'''
나의 점수     : {me_point}
컴퓨터의 점수 : {computer_point}
''')
        print()
        print('-' *50)
        print()

    else:
        computer_point += 1
        print('''
---------------------
| 나의 패배...ㅠㅠㅠ |
---------------------              
''')
        
        print()
        print('-' *50)
        print()
        print(f'''
나의 점수     : {me_point}
컴퓨터의 점수 : {computer_point}
''')
        print()
        print('-' *50)
        print()