char = input("영문 대문자 또는 소문자 하나를 입력하세요 : ")
char_ = char.upper()

if char_ == "A" or char_ == "E" or char_ == "I" or char_ == "U" or char_ == "O":
    print(f'{char} -> 모음')
    
else:
    print(f'{char} -> 자음')