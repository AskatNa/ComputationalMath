import math
a = 0
b = 2
nmax = 7
tol = 0.01
def f(x):
    return x**2 - x
def samesign(x,y):
    return (x * y) > 0;
def bisection(a,b,tol,nmax):
    c = (a + b) / 2
    fc = f(c)
    i = 0;
    while abs(fc > tol) and i <= nmax:
        if samesign(fc,f(a)):
            c = a
            b = b
        else:
            b = c
            a = a
        i += 1
    return c;
root = bisection(a,b,tol,nmax);
print("Root: ", root);

