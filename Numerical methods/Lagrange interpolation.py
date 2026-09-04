x=[]
y=[]
n=int(input('Enter the value n (keep it in mind n starts from 0):  '))
x1=float(input('Enter the value of X: '))
i=0
while i<(n+1):
    a=float(input('Enter the value of x(Given): '))
    x.append(a)
    i=i+1
print(x)

i=0
while i<(n+1):
    a=float(input('Enter the value of y(Given): '))
    y.append(a)
    i=i+1
print(y)
sumx=0
for i in range(0,(n+1)):

     pod=1
     for j in range(0,(n+1)):
        if j==i:
            continue
        pod=pod*((x1-x[j])/(x[i]-x[j]))
     sumx=sumx+pod*y[i]
print('The value of y(',x1,')',sumx)
    

