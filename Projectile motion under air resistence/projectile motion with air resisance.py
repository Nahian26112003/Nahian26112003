# NAHIAN
#projectile with air resistance
#shooting an object near an earth surface means g wull be approximately uniform
#Intial point (xo,y,)=(0,0)
#We take the force to be F=-kmv and so acceleration would be a=-kv and we can think k as a
#resistance property of the medium
import numpy as np
from matplotlib import pyplot as plt
v0=float(input('Enter the value of Vo or initial velosity: '))
theta_input=float(input('Enter the value of theta (in degree): '))
t0=float(input('Enter the value of to : '))
tf=float(input('Enter the value of tf (it is for air resistance): '))
dt=float(input('Enter the value of dt: '))
k=float(input('Enter the value of k: '))
g=9.8# m/s^2
theta_out=((theta_input)*((np.pi)/180))
v0x=v0*(np.cos(theta_out))
v0y=v0*(np.sin(theta_out))
t=t0
x1=[]
y1=[]
vx_t=[]
vy_t=[]
t1=[]
while t<=tf:
    t1.append(t)
    x=(v0x/k)*(1-(np.exp(-k*t)))
    x1.append(x)
    y=((1/k)*(v0y+(g/k))*(1-(np.exp(-k*t))))-((g/k)*t)
    y1.append(y)
    vx=v0x*(np.exp(-k*t))
    vx_t.append(vx)
    vy=((v0y+(g/k))*(np.exp(-k*t)))-(g/k)
    vy_t.append(vy)
    t=t+dt





#______________________________________________________________________
#for no air resistance
x2=[]
y2=[]

t=0
tf2=(2*v0y)/g
while t<=tf2:
    x=(v0x*t)
    x2.append(x)
    y=(v0y*t)-((0.5)*g*t**2)
    y2.append(y)
    t=t+dt
#___________________________________________________________________    
plt.plot(x1,y1,lw=1,label='for k='+str(k))
plt.legend(loc='upper right',fontsize=9)

plt.plot(x2,y2,lw=.7,label='for k=0')
plt.legend(loc='upper right',fontsize=9)
plt.xlim(0,15)
plt.ylim(0,5)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.savefig("X vs y.png",dpi=600)#by dpi I can control the resoulution
plt.show()



fig,axes=plt.subplots(1,2,figsize=(10,4))
ax=axes[0]
ax.plot(t1,x1,label='x(t)')
#ax.set_xlabel('x')
ax.plot(t1,y1,label='y(t)')
ax.set_xlabel('time t(sec)')
ax.legend()
ax=axes[1]
ax.plot(t1,vx_t,label='vx(t)')
ax.plot(t1,vy_t,label='vy(t)')
ax.set_xlabel('time t(sec)')
ax.legend()
plt.savefig("x,y vs t and vx,vy vs t.png",dpi=600)#by dpi I can control the resoulution
plt.show()










