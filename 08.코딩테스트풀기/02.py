def solution(a, d, included):
    result = 0
    for i in range(len(included)):
        if included[i]:
            result = result + (a + (d * i))
    return result

print(solution(3, 4, [True, False, False, True, True]))
print(solution(7, 1, [False, False, False, True, False, False, False]))