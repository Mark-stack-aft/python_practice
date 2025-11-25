temp = {'월' : 15.5, '화' : 17.0, '수' : 16.2, '목' : 12.9, '금' : 11.0, '토' : 10.5, '일' : 13.3}

print('-' * 50)
print()

for day in temp:
    print(f'{day:^6}', end = '')

print()
print()
print('-' * 50)
print()

for tp in temp:
    print(f'{temp[tp]:^6.1f}', end = ' ')

print()
print()
print('-' * 50)
print()

low_temp = ['월', temp['월']]

for lt in temp:
    if temp[lt] < low_temp[1]:
        low_temp = [lt, temp[lt]]

print('요일 : %s, 최저 기온 : %.1f °' %(low_temp[0], low_temp[1]))
print()

sum = 0

for st in temp:
    sum = sum + temp[st]

avg = sum/len(temp)

print('일주일간 기온 평균 : %.1f °' % avg)