width = int(input("사각형의 너비는? ")) #입력값 받기
height = int(input("사각형의 높이는? ")) #입력값 받기
length = 2 * width + 2 * height #둘레 길이 구하기
area = width * height #너비 * 높이를 하여 면적 구하기

print("사각형의 너비 : %dcm" % width) #사각형 너비 출력하기
print("사각형의 높이 : %dcm" % height) #사각형 높이 출력하기
print("둘레 길이 : %dcm" % length) #둘레 길이 출력하기
print("면적 : %dcm2" % area) #연적 출력하기