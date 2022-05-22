def inc(x):
    return x + 1

def double(f):
    return (lambda x : (f(f(x))))

print((double(double))(inc)(0))
