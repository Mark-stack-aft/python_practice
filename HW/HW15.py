num = 1
count = 0

while num <= 1000:
    if num % 3 != 0:
        print('%5d' % num, end = ' ')

        count += 1

    if count % 10 == 0:
        print()

    num += 1