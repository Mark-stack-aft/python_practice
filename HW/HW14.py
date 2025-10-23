factorial = 1
sum_factorial = 1

while factorial <= 10:
    sum_factorial *= factorial

    factorial += 1

print('10! =', sum_factorial)