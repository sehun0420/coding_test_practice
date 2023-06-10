def solution(numLog):
    result = ''
    for i in range(1, len(numLog)):
        a = numLog[i] - numLog[i-1]
        if a == 1:
            result += 'w'
        elif a == -1:
            result += 's'
        elif a == 10:
            result += 'd'
        elif a == -10:
            result += 'a'
    return result