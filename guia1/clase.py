import matplotlib.pyplot as plt
import numpy as np

a=np.array([[1,0,-1,0],[0,1,0,0],[-1,0,1,0],[0,0,0,1]])
print(a)

def posiblesvectores(vector,n,matriz,elegido):
    if(n==4):
        if(reconocevector(matriz,vector)):
            elegido=vector


        
        





def reconocevector(m,v):
    ret=(v.transpose())*m*v
    aux=(v.transpose())*v
    if(ret==0 and aux!=0):
        return True
    return False
        





        

