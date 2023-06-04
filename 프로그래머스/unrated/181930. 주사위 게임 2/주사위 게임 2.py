def solution(a, b, c):
    if a == b == c:
        return (a + b + c)*(a*a + b*b + c*c)*(a**3 + b**3 + c**3)
    elif a != b and a != c:
        if b != c:
            return (a + b + c)
        else:
            return (a + b + c)*(a*a + b*b + c*c)
    elif a == b or a == c:
        if b != c:
            return (a + b + c)*(a*a + b*b + c*c)