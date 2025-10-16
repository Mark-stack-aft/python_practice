start_num = int(input('시작 수를 입력해주세요 : '))
end_num = int(input('끝 수를 입력해주세요 : '))

for i in range(start_num, end_num):
    num = 0
    for s in range(2, i - 1):
        if i % s == 0:
            num += 1
    if num == 0:
        print(i, end = ' ')