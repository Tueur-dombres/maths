def P(x):return 2*x**3 + 3*x**2 + 1
def dicho(a,b,e):
    while b-a > e:
        m = (a+b)/2
        print(a,b,b-a,m,P(m)*P(a))
        if P(a)*P(m)<0:
            b=m
        else:
            a=m
    m=(a+b)/2
    print(a,b,b-a,m,P(m)*P(a))
    return a,b
print(dicho(-2,-1,0.1))