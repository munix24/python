#https://math.stackexchange.com/questions/238047/reversing-an-arithmetic-sequence
#https://www.programiz.com/python-programming/examples/quadratic-roots

def quad_eq(a, b, c):
    """
    returns both solutions to quadratic equation given a, b, c
    """
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    sol1 = (-b-d**.5)/(2*a)
    sol2 = (-b+d**.5)/(2*a)
    return [sol1,sol2]

def arithmetic_series(n, start = 0, end = 1):
    if start:
        return n * (start + end) / 2
    else:
        return n * (n + end) / 2

def inverse_arithmetic_series(n):
    """
    returns the inverse of arithmetic series using quadratic equation
    returns x where n = x (x + 1) /2
    """
    return quad_eq(1, 1, -(n*2))[1]#.real

print(inverse_arithmetic_series(5))
##print(arithmetic_series(4))
