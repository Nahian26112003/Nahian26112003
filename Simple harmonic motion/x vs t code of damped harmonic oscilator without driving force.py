import numpy as np
from matplotlib import pyplot as plt

#Section: 1
#======================================================================================================
#This section is for calculating and ploting displacement vs t graph of a SHO with damping and without
#driving force
#======================================================================================================
g=float(input("Enter the value of gamma: "))
omeganot=float(input("Enter the value of Omeganot: "))





x0=float(input("Enter the value of X0: "))
t0=float(input("Enter the value of t0: "))
tf=float(input("Enter the value of tf: "))
v0=float(input("Enter the value of V0: "))
h=float(input("Enter the value of h: "))
n=((tf-t0)/h)
n=round(n,1)
n=int(n)
vin=v0
tin=t0
xin=x0




for j in range(1,5):

 g=g/j
 g=round(g,2)
 def f1(v,t,x):
     
  z=v+(x*0)+(t*0)
  return z

 def f2(v,t,x):
     
  y=(-v*g)-(((omeganot)**2)*x)+(t*0)
  return y









 
 xplot=[]
 vplot=[]
 tplot=[] 

 v0=vin
 t0=tin
 x0=xin

 
 
 for i in range(1,n+1):
  tplot.append(t0)
  k1=f1(v0,t0,x0)
  l1=f2(v0,t0,x0)
  k2=f1((v0+(l1*h/2)),(t0+(h/2)),(x0+(k1*h/2)))      
    
  l2=f2((v0+(h*l1/2)),(t0+(h/2)),(x0+(h*k1/2)))
  k3=f1((v0+(h*l2/2)),(t0+(h/2)),(x0+(h*k2/2)))

  l3=f2((v0+(h*l2/2)),(t0+(h/2)),(x0+(h*k2/2)))
  k4=f1((v0+h*l3),(t0+h),(x0+h*k3))
    
            
  l4=f2((v0+h*l3),(t0+h),(x0+h*k3))

  x=x0+(h/6)*(k1+(2*(k2))+(2*k3)+k4)
  v=v0+(h/6)*(l1+(2*(l2))+(2*l3)+l4)
  xplot.append(x)
  vplot.append(v) 
  v0=v
  x0=x
  t0=(t0+h)

 

 plt.plot(tplot,xplot,label='Gamma='+str(g))

 #plt.plot(xplot,vplot,label='Gamma='+str(g))
 
 #tplot. clear()
 #vplot. clear()
 #xplot. clear()
 print(g)

plt.legend(loc='upper right',fontsize=9)



#plt.xlim(0,15)
#plt.ylim(0,5)
plt.xlabel('t')
plt.ylabel('x(t)')
 

 


plt.savefig("X vs t.png",dpi=600)#by dpi I can control the resoulution
plt.show()


 

        






















    
    
        

    
