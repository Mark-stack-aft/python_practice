def solution(n, t):
    result = n
    for i in range(t):
        result = result * 2
    return result

print(solution(2, 10))
print(solution(7, 15))