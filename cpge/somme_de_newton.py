coeffs = list(map(float,input().split()))
es = [-coeffs[i]/coeffs[0] if i%2 else coeffs[i]/coeffs[0] for i in range(1,len(coeffs))]
n = 10
n = int(input())
ps = []
for i in range(n):
    ps += [sum((-1 if j%2 else 1)*(es[j] if j < len(es) else 0)*(ps[i-j-1] if i!=j else i+1) for j in range(i+1))]
print(ps)