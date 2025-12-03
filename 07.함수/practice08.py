def cir_area():
    global r
    result = r * r * 3.14
    return result

def cir_lenth():
    global r
    result = 2 * 3.14 * r
    return result

r = float(input('반지름을 입력하세요 : '))

area = cir_area()
lenth = cir_lenth()

print('원의 면적 : %.1f, 원주의 길이 : %.1f' % (area, lenth))