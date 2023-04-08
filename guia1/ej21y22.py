import matplotlib.pyplot as plt
import numpy as np
import math

v1=np.array([0,0])
v2=np.array([1,0])
v3=np.array([0,1])
v4=np.array([1,1])

# v1=matriz.dot(v1)
# v2=matriz.dot(v2)
# v3=matriz.dot(v3)
# v4=matriz.dot(v4)

listavectores=[v1,v2,v3,v4]

def escalar(vectores,a,b):
    matriz=np.array([[a,0],[0,b]])
    i=0
    while (i<len(vectores)):
        vectores[i]=matriz.dot(vectores[i])
        i+=1
    return vectores

def rotacion(vectores,gamma):
    matriz=np.array([[math.cos(gamma),-math.sin(gamma)],[math.sin(gamma),math.cos(gamma)]])
    i=0
    while (i<len(vectores)):
        vectores[i]=matriz.dot(vectores[i])
        i+=1
    return vectores


vectores=rotacion(listavectores,0.45)
vectores=escalar(vectores,5,5)
    


x1=[vectores[0][0],vectores[1][0],vectores[2][0],vectores[3][0]] 

y1=[vectores[0][1],vectores[1][1],vectores[2][1],vectores[3][1]] 

x0=[0,0,0,0]
y0=[0,0,0,0]

plt.title("Matplotlib demo") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.axhline(0, color="black")  
plt.axvline(0, color="black")
plt.quiver(x0,y0,x1,y1, angles='xy', scale_units='xy', scale=1)
plt.grid(True)
plt.xlim([-10,10])
plt.ylim([-10,10])
plt.show()




