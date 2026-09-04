def f(x,y):
    #z=y-z
    z=1+(y**2)
    return z
x0=float(input("Enter the value of Xo: "))
y0=float(input("Enter the value of Yo: "))
a=float(input("Enter the value of X: "))
h=float(input("Enter the value of h: "))

n=((a-x0)/h)
n=round(n,1)
n=int(n)
for i in range(1,n+1):
    k1=h*f(x0,y0)
    k2=h*f((x0+(h/2)),(y0+(k1/2)))
    k3=h*f((x0+(h/2)),(y0+(k2/2)))
    k4=h*f((x0+h),(y0+k3))
    y1=y0+((1/6)*(k1+(2*k2)+(2*k3)+k4))
    x0=x0+h
    y0=y1
print('the value of y(',a,')',y1)
