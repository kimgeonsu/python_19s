import math as m
def solver(a,b,c) :
    t1=(-b+m.sqrt(b**2-4*a*c))/2*a
    t2=(-b-m.sqrt(b**2-4*a*c))/2*a
    print(t1,t2)

solver(1,50,-150)
