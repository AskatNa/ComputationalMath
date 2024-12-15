x0 = 1
x1 = 2
tol = 0.01
nmax = 10
def f(x):
    return x**3 - x - 1
def sign(x0,x1): #step 3
    fx0 = f(x0)
    fx1 = f(x1)
    if fx1 * fx0 < 0:
        return True
    else:
        return False
def secantMethod(x0,x1,tol,nmax): #step 1
    for i in range(nmax):
        fx0 = f(x0)
        fx1 = f(x1)
        sign(fx0,fx1) # step 3
        x2 = x1 - fx1 * ((x1 - x0) / (fx1 - fx0)) # step 4
        print(f"Iteration {i}: x = {x2}")
        if abs(x2 - x1) > tol: #step 5
            x0 = x1
            x1 = x2
        elif abs(x2 - x1) < tol:
            return x2
        else:
            return x2
root = secantMethod(x0,x1,tol,nmax)
print("x2 root: ", root) # step 6

