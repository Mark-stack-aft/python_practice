#딕셔너리
score = {'kor' : 90, 'eng' : 45}
print(score)

#추가
score['math'] = 100
print(score)

#수정
score['eng'] = 80
print(score)

#삭제
x = score.pop('math')
print(x)
print(score)

#초기화
score.clear()
print(score)