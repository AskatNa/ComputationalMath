x0 = 1
tol = 0.00001
nmax = 100
def g(x):
    return (x+1)**(1/3)
def iterationMethod(x0,tol,nmax):
    x = x0
    for i in range(1, nmax + 1):
            fx = g(x)
            print(f"Iteration {i}: x = {fx}")

            if abs(fx - x) < tol:
                print(f"Solution found: x = {fx}")
                return fx
            x = fx

    print("Solution doesn't converge")
    return None

root = iterationMethod(x0,tol,nmax)
print("Root: ", root)