import numpy as np
from matplotlib import pyplot as plt

#Section: 1
#======================================================================================================
#This section is for calculating and ploting displacement vs t graph of a SHO with damping and with
#driving force
#======================================================================================================
xl0=[]
vl0=[]
for k in range(1,3):
 x0=float(input("Enter the value of x0: "))
 v0=float(input("Enter the value of v0: "))
 xl0.append(x0)
 vl0.append(v0)
#Now xl0[0],xl0[1] will be the two initail displacement input. This is
 #same for vl0[]





g=float(input("Enter the value of gamma: "))
omeganot=float(input("Enter the value of Omeganot: "))
omega=float(input("Enter the value of Omega: "))
a0=float(input("Enter the value of a0 (the value of amplitude of driving force): "))





t0=float(input("Enter the value of t0: "))
tf=float(input("Enter the value of tf: "))

h=float(input("Enter the value of h: "))
n=((tf-t0)/h)
n=round(n,1)
n=int(n)
#vin=v0
tin=t0
#xin=x0




for j in range(0,2):

 v0=vl0[j]
 x0=xl0[j]
 def f1(v,t,x):
     
  z=v+(x*0)+(t*0)
  return z

 def f2(v,t,x):
     
  y=(-v*g)-(((omeganot)**2)*x)+ (a0*(np.cos(omega*t)))
  return y









 
 xplot=[]
 vplot=[]
 tplot=[] 

 
 t0=tin
 

 
 
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

 

 plt.plot(tplot,xplot,label='x0='+str(xl0[j]) + ' v0='+str(vl0[j]))

 
 
 #tplot. clear()
 #vplot. clear()
 #xplot. clear()
 print(g)

plt.legend(loc='upper right',fontsize=9)



#plt.xlim(0,15)
#plt.ylim(0,5)
plt.xlabel('t')
plt.ylabel('x(t)')
 

 


plt.savefig("X vs t with driving force.png",dpi=600)#by dpi I can control the resoulution
plt.show()

#===========================================================================
#This section is for amplitude
#=========================
print('Now Enter Gamma for amplitude vs omega plot')
gammanw=float(input("Enter the value of gamma: "))
omeganw=np.arange(0,5,0.01)
amplitude =a0/((((((((omeganot)**2) - ((omeganw)**2))**2))**2)+((gammanw*omeganw)**2))**0.5)
plt.plot(omeganw,amplitude)
plt.xlabel('omega')
plt.ylabel('amplitude')
plt.savefig("amplitude  vs omega of driving force.png",dpi=600)        






















    
    
        

    
