def f(x):
    z=1/(1+x)
    return z
trapi=[]
x0=float(input('Enter the value of Xa: '))
x1=float(input('Enter the value of Xb: '))
h=float(input('Enter the value of h' ))
m=int(input('Enter the number of stepsizes'))

for i in range(1,(m+1)):
    sumx=0
    n=(x1-x0)/h
    n=round(n,1)
    n=int(n)
    for j in range(1,n):
       x=x0+j*h
       sumx=sumx+f(x)
    inte=(h/2)*(f(x0)+f(x1)+(2*sumx))

    trapi.append(inte)
    print(inte)
    h=h/2

#print(trapi[1])
romb=[]
for k in range (1,m):
    rombformula=(1/3)*((4*trapi[k])-trapi[k-1])
    romb.append(rombformula)

    print(rombformula)
l=0
m=m-2
rombfin=[]
while True:
   if m==0:
       break
   l=l+1
   
   rombfindummy=(1/3)*(4*romb[l]-romb[l-1])
   print(rombfindummy)
   rombfin.append(rombfindummy)
   if l==m:
       m=m-1
       l=0
       rombfin[l]=romb[l]
       




















