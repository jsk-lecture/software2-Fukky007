def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def cube(x):
    return x*x*x

def integral(f, a, b, dx):
    def add_dx(x): return x + dx
    return sum(f, a + (dx/2.0), add_dx, b) * dx

def simpson(f, a, b, n):
    h = float(b - a) / n
    def y(k):
        return f(a + k*h)
    
    def term(k):
        if k == 0 or k == n:
            return y(k)
        elif k%2 == 0:
            return 2*y(k)
        elif k%2 == 1:
            return 4*y(k)
        
    return sum(term, a, lambda x : x + 1, n / (b - a)) * h / 3.0

n = 5
print('n = %d\t --> integral:%lf, simpson:%lf' % (n,integral(cube, 0, 1, 1/n), simpson(cube, 0, 1, n)))

n = 10
print('n = %d\t --> integral:%lf, simpson:%lf' % (n,integral(cube, 0, 1, 1/n), simpson(cube, 0, 1, n)))

n = 100
print('n = %d\t --> integral:%lf, simpson:%lf' % (n,integral(cube, 0, 1, 1/n), simpson(cube, 0, 1, n)))
