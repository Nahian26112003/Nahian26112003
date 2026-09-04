def f(x,y):
    z=y+(x**2)
    return z
x0=float(input("Input the value of Xo :"))
y0=float(input("Input the value of Yo :"))
x1=float(input("Input the value of X  :"))
h=float(input("Input the value of h :(stepsize)"))
n=(x1-x0)/h
n=round(n,1)
n=int(n)
for i in range(1,(n+1)):
   y1=y0+h*(f(x0,y0))
   x=x0+i*h
   y0=y1
   y0=round(y0,4)
   x0=x

print('The y(',x,')',y0)
#print(y1)
