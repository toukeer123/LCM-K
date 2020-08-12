def cube(x,y):
    c_val = []
    for i in range(len(x)):
        z = x[i]**y
        c_val.append(z)
    return c_val
def gcd(P,Q): 
    if P == 0: 
        return Q 
    return gcd(Q % P, P) 
def lcm(q,d): 
    Z = 0
    for i in range(0,len(q)-1):
        Z = (q[i]*q[i+1]) / (gcd(q[i],q[i+1]))
    Z = Z%d
    return Z
p = []
T =int(input())
NMK = list(map(int,input().split()))
a = list(map(int,input().split()))
if(T>=1 and T<=10):
    if(NMK[0]>=1 and NMK[0] <= 3*(10**5)):
        if(NMK[1] >= 1):
            if(NMK[2] <= (10**9)):
                p = cube(a,NMK[2])
                X = lcm(p,NMK[1])
                print(int(X))