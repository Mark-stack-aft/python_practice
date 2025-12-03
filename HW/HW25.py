def make_square_list(n):
    square_list = []

    for square in range(n):
        square_list.append((square + 1) ** 2)

    return square_list

n = int(input('n 의 값을 입력하세요 : '))

print(make_square_list(n))