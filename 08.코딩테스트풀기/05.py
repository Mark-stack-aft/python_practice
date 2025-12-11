def solution(n):
    pizza_cut = 0
    while True:
        pizza_cut = pizza_cut + 1
        if (pizza_cut * 6) % n == 0:
            break
    return pizza_cut

print(solution(10))