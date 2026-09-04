def f(x):
    z=1/(1+x)
    return z
x0=float(input('Enter the value of a: '))
x1=float(input('Enter the value of b: '))
h=float(input('Enter the value of stepsize h: '))
n=(x1-x0)/h
n=round(n,1)
sumx=0
n=int(n)
print('n=',n)
for i in range(1,n):
  x=x0+(i*h)
  
  sumx=sumx+f(x)
  #print('x=',x)
  #print('f(x)=',f(x))
#print('sumx=',sumx)
trapi=((h/2)*(f(x0)+f(x1)+(2*sumx)))
print('Value of integration is I=',trapi)
