import matplotlib.pyplot as plt
import numpy as np
import math
#Ejercicio 7
b1=1
x1=np.array(range(100))
y1=(1.5*x1-b1/2)

b2=40
x2=np.array(range(100))
y2=(1.5*x2-b2/4)

plt.plot(x1,y1,color="r",label="ec1")
plt.plot(x2,y2,color="g",label="ec2")
plt.xlabel("Angle")
plt.ylabel("Magnitude")
plt.title("Sine and Cosine functions")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()

#Este sistema o no tiene solucion o tiene infinita soluciones dado que son paralelas

############################################################################################3




