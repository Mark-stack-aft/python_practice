def average(*args):
    num_ages = len(args)
    sum = 0

    for i in range(num_ages):
        sum += args[i]

    avg = sum / num_ages

    print(f'합계 : {sum}')
    print(f'평균 : {avg}')

average(1, 2, 3, 4)