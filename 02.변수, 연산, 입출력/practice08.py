print('hello world \n hi')
print('hello world \t hi')
print('hello python')


kor = input("국어 성적을 입력하세요: ")
eng = input("영어 성적을 입력하세요: ")
math = input("국어 성적을 입력하세요: ")

sum = int(kor) + int(eng) + int(math)

avg = sum/3

print('합계: %d, 평균: %.0f' %(sum, avg))