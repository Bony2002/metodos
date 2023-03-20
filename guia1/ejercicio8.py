import matplotlib.pyplot as plt
import numpy as np

x1=np.array(range(-100,100))
y1=3*x1+5

#plt.plot(x1,y1,color="r",label="ec1")


x2=np.array(range(-100,100))
y2=((x2**2)/25)-2*x2+10
#plt.plot(x2,y2,color="b",label="ec2")

x31=np.array(range(-100,0))
y31=-10*x31+5
x32=np.array(range(0,100))
y32=10*x32+5

plt.plot(x31,y31,color="b",label="ec1")
plt.plot(x32,y32,color="y",label="ec2")

plt.legend()
plt.show()