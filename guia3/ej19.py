import matplotlib.pyplot as plt
import numpy as np
import random as rm

# e=0.01
# mx=np.array([[1,1+e],[1-e,1]])
# v=np.random.randint(1,89,size=(2,1))

# print(np.linalg.cond(mx))

# res=np.linalg.solve(mx,v)

# print(res)
# Mientras e es mas chico, mas grande son los numeros de x que generan esa respuesta


# mx=np.array([[4.5,3.1],[1.6,1.1]])
# b1=np.array([19.249,6.843])
# b2=np.array([19.25,6.84])
# res1=np.linalg.solve(mx,b1)
# res2=np.linalg.solve(mx,b2)
# print(res1)
# #x1 = 3.94
# #x2 = 0.48999999999999996489
# print(res2)

# print(np.linalg.cond(mx))

# mx=np.array([[4,0,-7,-7],[-6,1,11,9],[7,-5,10,19],[-1,2,3,-1]])
# x=np.random.random((4,1))
# print(x)
# b=mx.dot(x)
# #print(b)
# xp=np.linalg.solve(mx,b)
#print(xp)

#D = np.array([[5, 3, 1, 7, 9], [6, 4, 2, 8, -8], [7, 5, 3, 10, 9], [9, 6, 4, -9, -5], [8, 5, 2, 11, 4]])
#print(D)

mx=np.arange(600).reshape([20,30])
sb=np.arange(50).reshape([5,10])
# print(sb)

def submatriz(mx, f1,f2,c1,c2):
    c1-=1
    c2-=1
    f1-=1
    f2-=1
    sb=mx[f1:f2,c1:c2]
    return sb

def reemplazar(mx,sb,f1,f2,c1,c2):
    c1-=1
    c2-=1
    f1-=1
    f2-=1
    mx[f1:f2,c1:c2]=sb
    return mx

def agrandar(mx):
    mxt=mx.transpose()
    ret=np.zeros([50,50])
    ret[0:29,0:19]=mx
    ret[20:49,30:49]=mxt

# sb2=submatriz(mx,1,3,1,4)
# mx2=reemplazar(mx,sb,5,10,10,20)
# print(sb)
# print(mx[4:9,9:19])

def dividir(mx):
    mx1=mx[0:25,0:25]
    mx2=mx[0:25,25:50]
    mx3=mx[25:50,0:25]
    mx4=mx[25:50,25:50]
    lx=list()
    lx.append(mx1)
    lx.append(mx2)
    lx.append(mx3)
    lx.append(mx4)
    return lx
A=np.arange(2500).reshape(50,50)
B=np.arange(2500).reshape(50,50)
AP=dividir(A)
BP=dividir(B)
# print(Amx[0])   
# print(Amx[1])
print(AP[3]) 

def suma(A,B):
    AP=dividir(A)
    BP=dividir(B)
    mx=np.zeros(50)
    mx[0:25,0:25]=AP[0]+BP[0]
    mx[0:25,25:50]=AP[1]+BP[1]
    mx[25:50,0:25]=AP[2]+BP[2]
    mx[25:50,25:50]=AP[3]+BP[3]
    return(mx)


def multiplicacion(A,B):
    AP=dividir(A)
    BP=dividir(B)
    mx=np.zeros(50)
    mx[0:25,0:25]=AP[0]@BP[0]
    mx[0:25,25:50]=AP[1]@BP[1]
    mx[25:50,0:25]=AP[2]@BP[2]
    mx[25:50,25:50]=AP[3]@BP[3]
    return(mx)

