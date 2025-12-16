def solution(num_list):
    count = 0
    for num in num_list:
        now_num = num
        while True:
            if now_num == 1:
                break
            if not now_num % 2 == 0:
                now_num = now_num - 1
            now_num = now_num / 2
            count = count + 1
    return count

print(solution([12, 4, 15, 1, 14]))