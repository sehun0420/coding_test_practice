def solution(a, d, included):
    num = a
    sum = 0
    for i in range(len(included)):
        if included[i] == True:
            sum += num
        num += d
    return sum