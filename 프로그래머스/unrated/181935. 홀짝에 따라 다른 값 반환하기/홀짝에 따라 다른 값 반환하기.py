def solution(n):
    total = 0
    a = 1
    b = 2
    if n % 2 != 0:
        while a <= n:
            total += a
            a += 2
    else:
        while b <= n:
            total += b*b
            b += 2
    return total