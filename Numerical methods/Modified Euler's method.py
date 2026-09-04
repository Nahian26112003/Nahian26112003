def f(x,y):
    z=y+(x**2)
    #z=3*x+(y/2)
    return z
x0=float(input("Input the value of Xo: "))
y0=float(input("Input the value of Yo :"))
xin=float(input("Input the value of X: "))
h=float(input("Input the value of h :(stepsize) "))
#y0=round(y0,4)
#x0=round(x0,4)
#xin=round(xin,4)
n=(xin-x0)/h
n=round(n,1)
n=int(n)
m=int(input('Enter the value of the number of iteration: '))
for i in range(1,(n+1)):
   y1=y0+h*(f(x0,y0))
   #y1=round(y1,4)
   x1=x0+i*h
   for j in range(1,(m+1)):
       y1modi=y0+((h/2)*(f(x0,y0)+f(x1,y1)))
       y1=y1modi
       #y1=round(y1,4)
   
   x0=x1
   y0=y1modi
   y0=round(y0,4)
print(y1)
