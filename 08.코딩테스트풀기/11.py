def solution(numLog):
    n = numLog[0]
    result = ''
    wsad = {1 : 'w', -1 : 's', 10 : 'd', -10 : 'a'}
    for x in range(1, len(numLog)):
        result = result + wsad[numLog[x] - n]
        n = numLog[x]
    return result

print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))