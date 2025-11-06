list = [[1, 2, 3], [4, 5, 6]]

print(list[1][0])

print(list[0][1])

for first_index in list:
    for second_index in first_index:
        print(second_index, end = ' ')