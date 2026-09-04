def f(x,y):
    z=y-x
    return z
x0=float(input("Enter the value of Xo: "))
y0=float(input("Enter the value of Yo: "))
a=float(input("Enter the value of X: "))
h=float(input("Enter the value of h: "))
n=((a-x0)/h)
n=round(n,1)#this rounding is important because when
#i take x=.3 the n becomes 2.999999996. and when
#I round this I get 2 insted of 3. so a very error occurs
n=int(n)


for i in range(1,n+1):
    k1=h*f(x0,y0)
    k2=h*f((x0+h),(y0+k1))
    y1=y0+((0.5)*(k1+k2))
    print(y1)
    
    x0=x0+h
    
    y0=y1
    

print('the value of y(',a,')','=',y1)
