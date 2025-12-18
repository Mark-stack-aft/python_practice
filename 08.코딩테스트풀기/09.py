def solution(arr, intervals):
    return arr[intervals[0][0] : intervals[0][1] + 1] + arr[intervals[1][0] : intervals[1][1] + 1]

print(solution([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))