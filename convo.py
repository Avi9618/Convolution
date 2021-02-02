import numpy as np
p=[1,2,3,4]
q=[2,3,4]
lp=len(p)
lq=len(q)
l=max(lp,lq)
x1=np.zeros(l)
x2=np.zeros(l)
x3=np.zeros(l)

for i in range(0,lp):
    x1[i]=p[i]
    
for j in range(0,lq):
    x2[j]=q[j]
    
if lp>lq:
    print 'x1>x2 \n padding zeros to x2',x2,'\n'
else:
    print 'x1<x2 \n padding zeros to x1',x1,'\n'
    
def r(x):
    z=np.zeros(l)
    z[0]=x[0]
    for i in range(0,l-1):
        i=i+1
        z[i]=x[l-i]
    z=np.array(z)
    return z
    
for i in range(0,l):
    a=np.roll(r(x2),i)
    print i,'.x1      ',x1,'\n'
    print i,'.x2(m-n) ',a,'\n'
    x3[i]=sum(x1*a)
    print i,'.x3      ',x3[i],'\n'
    
print x3
