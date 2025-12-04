def solution(n, control):
    result = n
    control_list = {'w' : 1, 's' : -1, 'd' : 10, 'a' : -10}

    for char in control:
        result = result + control_list[char]

    return result

print(solution(0, 'wsdawsdassw'))
print(solution(0, 'wsdawdsassw'))
print(solution(5, 'w'))
print(solution(3, 'wads'))
print(solution(-7, 'ddsa'))