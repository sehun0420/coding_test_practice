def solution(arr, queries):
    a = 0
    while a < len(queries):
        i = queries[a][0]
        j = queries[a][1]
        x = arr[i]
        y = arr[j]
        arr[i] = y
        arr[j] = x
        a += 1
    return arr