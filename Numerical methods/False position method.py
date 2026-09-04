import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
def f(x):
    z=((np.exp(-x))-x)
    return z


while True:
    
       a=float(input('Enter the value of X1: '))
       b=float(input('Enter the value of X2: '))
       print('f(',a,')=',f(a),      'f(',b,')=',f(b)     )
       if (f(a)*f(b))<0:
           print('The roots initial roots input is ok')
           print(a,b)
           print('Accepted roots X1,X2 are respecteviely',a,b)
           break
       else:
            print('Roots input are not correct')


if a>b:
    x1=b
    x2=a
else:
    x1=a
    x2=b
    
n=int(input('Enter the number of iteration n: '))
i=0

sol=[]
iti=[]

while i<n:
    x=x1+((x2-x1)*abs(f(x1)))/((abs(f(x1)))+(abs(f(x2))))
    if f(x)*f(x1)>0.0:
        x1=x
        x2=x2
    else:
        x2=x
        x1=x1
    print('Root for the intration number n=',i+1,'is','X=',x)
    i=i+1
    sol.append(x)
    iti.append(i)
plt.plot(iti,sol)
plt.xlabel('No of iteration')
plt.ylabel('Solution in terms of x')
plt.show()

fig,axis=plt.subplots()
axis.set_xlim([min(iti),max(iti)])
axis.set_ylim(0.3,1)
axis.grid(True)
animated_plot,= axis.plot([],[])

def update_data (frame):
 animated_plot.set_data(iti[:frame],sol[:frame])

 return animated_plot
animation=FuncAnimation(fig=fig,func=update_data,frames=len(iti),interval=5) #Ths line must be understood 
plt.show()







    
