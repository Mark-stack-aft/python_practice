score1 = int(input('필기 점수: '))
score2 = int(input('실기 점수: '))

if score1 >= 80 and score2 >= 80:
    result = '합격'

else:
    result = '불합격'

print(f'-필기 점수: {score1}')
print(f'-실기 점수: {score2}')
print(f'-판정: {result}')