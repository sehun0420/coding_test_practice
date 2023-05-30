def solution(a, b):
    c = 2 * a * b
    a = str(a)
    b = str(b)
    if int(a + b) > c:
        return int(a + b)
    else:
        return c