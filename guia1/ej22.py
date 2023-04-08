import matplotlib.pyplot as plt
import numpy as np
import math

n=3



def armaR(k,n):
    mtx=np.zeros((n,n)) 
    i=0
    while(i<n):
        if(i!=k):
            mtx[i][i]=1
        i+=1
    return mtx

test=armaR(1,4)
print(test)