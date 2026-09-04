def f(x):
    z=1/(1+x)
    return z
print('You must maintain b>a')
x0=float(input('Enter the value of a: '))
x1=float(input('Enter the value of b: '))
h=float(input('Enter the value of stepsize h: '))
n=(x1-x0)/h
n=round(n,1)
sumx1=0
n=int(n)

print('n=',n)
for i in range(1,n,2):
  x=x0+(i*h)
  sumx1=sumx1+f(x)
sumx2=0
for i in range(2,(n-1),2):
  x=x0+(i*h)
  sumx2=sumx2+f(x)
simpson=((h/3)*(f(x0)+f(1)+(4*sumx1)+(2*sumx2)))
print('The result of intergration is I =',simpson)
  
  

