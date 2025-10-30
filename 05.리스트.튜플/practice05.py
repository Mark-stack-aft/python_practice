animals = []

while True:
    name = input('동물 이름 입력 (종료 : 0): ')

    if name == '0':
        break

    animals.append(name)

print(f'동물 리스트 : {animals}')