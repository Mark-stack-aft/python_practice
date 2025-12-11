def solution(a, b, c):
    result = a + b + c
    if a == b or b == c or c == a:
        result = result * (a ** 2 + b ** 2 + c ** 2)
    if a == b == c:
        result = result * (a ** 3 + b ** 3 + c ** 3)
    return result

print(solution(2, 6, 1))
print(solution(5, 3, 3))
print(solution(4, 4, 4))

##### 테스트 케이스 #####

print('\n##### 테스트 케이스 #####\n')

print(solution(5, 5, 2))
print(solution(2, 5, 5))
print(solution(3, 3, 3))