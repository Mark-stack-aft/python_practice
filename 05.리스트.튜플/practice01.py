num = [1, 2, 3, 4, 5]
print(num)

# 추가
num.append(6)
print(num)

num.insert(2, 2.5)
print(num)

# 삭제
num.remove(2.5)
print(num)

num.pop()
print('pop부분', num)

num.pop(1)
print(num)

# 내림차순
num.reverse()
print(num)

# 오름차순
num.sort()
print(num)

# 최댓값
print(max(num))

# 최솟값
print(min(num))

# 합계
print(sum(num))

# 요소 찾기
print(num.index(4))