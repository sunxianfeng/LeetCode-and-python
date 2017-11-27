# -*- coding:utf-8 -*-
def f(x):
    return x*x*x*x

def GetA_Armijo(x,a):
    c1 = 0.3
    d = 4*x*x*x
    now = f(x)
    next = f(x-a*d)

    count = 10
    while next < now:
        a *= 2
        next = f(x-a*d)
        count -= 1
        if count == 0: break

    count = 10
    while next > now - c1*a*d*d:
        a /= 2
        next = f(x-a*d)
        count -= 1
        if count == 0: break

    return a,f(x-a*d)

if __name__ == "__main__":
    x = 1.5
    a = 0.1
    for _ in range(10):
        m,n = GetA_Armijo(x,a)
        a = m
        x = x-a*4*x*x*x
        print m,n
