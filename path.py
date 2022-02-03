import math
B={0:1,1:1,2:2,3:8}
def b(n):
    if n in B:
        return B[n]
    #v=(2*n-1)*b(n-1) - (n-1)*(n-1)*b(n-2) + (n-2)*(n-1)*b(n-3) - (n-3)*(((n-2)*(n-1))//2)*b(n-4)
    v=(n)*b(n-1)
    B[n]=v
    return v

def c(n,m):
    v=0
    s=0
    S=[]
    for i in range(1,m):
        s=math.comb(n-1,i)*math.factorial(i)*b(n-i-1)
        S.append(s)
        v+=s
    w=0
    for s in S:
        w+=s
        #print(s,s/v,(v-w)/v,m*s/v)
        #if(abs(((v-w)/v)-0.5)<0.05):
            #print(S.index(s))
    return v

def ca(n):
    return c(n,n-1)

k=1
mj=200
for i in range(5,200):
    print(i,(2*(i-4)*math.factorial(i-3)//2)/math.factorial(i))
