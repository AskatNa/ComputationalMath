x0 = 1
tol = 0.00001
nmax = 100
def f(x):
    return x**3 - x - 1
def df(x):
    return 3*x**2 - 1
def newtonRaphson(x0,tol,nmax):
    x = x0
    for i in range(1,nmax + 1):
        h = f(x) / df(x)
        x = x - h
        print(f"Iteration {i}: x = {x}")
        if abs(h) < tol:
            print(f"Solution found: x = {x}")
            return x

    print("Solution doesn`t converge")
    return None
root = newtonRaphson(x0,tol,nmax)
print("Root: ", root)