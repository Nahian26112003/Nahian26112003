import numpy as np
def f(x):
    z=((np.exp(-x))-x)
    return z


while True:
    
       x1=float(input('Enter the value of X1: '))
       x2=float(input('Enter the value of X2: '))
       print('f(',x1,')=',f(x1),      'f(',x2,')=',f(x2)     )
       if (f(x1)*f(x2))<0:
           print('The roots initial roots input is ok')
           print(x1,x2)
           print('Accepted roots X1,X2 are respecteviely',x1,x2)
           break
       else:
            print('Roots input are not correct')
n=int(input('Enter the number of iteration n: '))
i=0
while i<n:
 xr=(x1+x2)/2
# x.append(xr)
 
 if f(x1)*f(xr) >0:
    x1=xr
    x2=x2
 else:
    x1=x1
    x2=xr
 i=i+1
 print('Root is approximate root for n=',i,xr)
 #Pending Task is I have to show the approximate errors beside the approximate roots
            

        
