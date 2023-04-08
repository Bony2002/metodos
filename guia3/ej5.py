import matplotlib.pyplot as plt
import numpy as np
import random as rm


# m0=np.zeros([4,5])
# mi=np.identity(5)
# m1=np.full([5,3],1)

# print(m0)
# print(mi)
# print(m1)


# mx=np.zeros([4,4])
# np.fill_diagonal(mx,[3,4,2,5])
# print(mx)


# def matrizaleatoria(n,m,a,b):
#     mx=np.zeros([n,m])
#     i=0
#     while i<n:
#         j=0
#         while j<m:
#             mx[i][j]=rm.randint(a,b)
#             j+=1
#         i+=1
#     return mx


# mx=matrizaleatoria(6,4,-9,9)
# print(mx)

# A1=matrizaleatoria(4,4,129,213)
# A2=matrizaleatoria(4,4,-1213,9)
# A3=matrizaleatoria(4,4,909,1231)
# I=np.identity(4)


# R1=((A1+I)@(A1-I))-(A1@A1-I)
# R2=((A2+I)@(A2-I))-(A2@A2-I)
# R3=((A3+I)@(A3-I))-(A3@A3-I)

# print(R1)
# print(R2)
# print(R3)


# B1=matrizaleatoria(4,4,238,1290)
# B2=matrizaleatoria(4,4,-8,9)
# B3=matrizaleatoria(4,4,-123,4)



# V1=((A1+B1)@(A1-B1))-(A1@A1-B1@B1)
# V2=((A2+B2)@(A2-B2))-(A2@A2-B2@B2)
# V3=((A3+B3)@(A3-B3))-(A3@A3-B3@B3)

# print(V1)
# print(V2)
# print(V3)


# def potencia(mx,k):
#     i=1
#     while i<k:
#         mx=mx@mx
#         i+=1
#     return mx

# mx=np.zeros([5,5])
# mx[0][1]=1
# mx[1][2]=1
# mx[2][3]=1
# mx[3][4]=1
# print(mx)

# for k in range(2,6):
#     print(potencia(mx,k))

# mx=np.zeros([3,3])
# mx[0][0]=1/6
# mx[0][1]=1/2
# mx[0][2]=1/3
# mx[1][0]=1/2
# mx[1][1]=1/4
# mx[1][2]=1/4
# mx[2][0]=1/3
# mx[2][1]=1/4
# mx[2][2]=5/12

# print(potencia(mx,5))
# print(potencia(mx,10))
# print(potencia(mx,20))
# print(potencia(mx,30))

# Estas potencias van disminuyendo al punto que llegan a 0

def vectores():
    vectores=[0]*16
    vectores[0]=np.array([0,0,0,0])
    vectores[1]=np.array([0,0,0,1])
    vectores[2]=np.array([0,0,1,0])
    vectores[3]=np.array([0,0,1,1])
    vectores[4]=np.array([0,1,0,0])
    vectores[5]=np.array([0,1,0,1])
    vectores[6]=np.array([0,1,1,0])
    vectores[7]=np.array([0,1,1,1])
    vectores[8]=np.array([1,0,0,0])
    vectores[9]=np.array([1,0,0,1])
    vectores[10]=np.array([1,0,1,0])
    vectores[11]=np.array([1,0,1,1])
    vectores[12]=np.array([1,1,0,0])
    vectores[13]=np.array([1,1,0,1])
    vectores[14]=np.array([1,1,1,0])
    vectores[15]=np.array([1,1,1,1])
    return vectores




def testeo(mx):
    v=vectores()
    for i in v:
        res=i.transpose()@mx@i
        aux=i.transpose()@i
        print(res)
        # print(aux)
        if res==0 and aux.any():
            return i
    return False


mx=np.zeros([4,4])
np.fill_diagonal(mx,1)
mx[0][2]=-1
mx[2][0]=-1
print(mx)
print(testeo(mx))
mx=np.zeros([4,4])
np.fill_diagonal(mx,1)
mx[0][3]=-1
mx[1][3]=-1
mx[3][0]=-1
mx[3][1]=-1
mx[3][3]=2
print(mx)
print(testeo(mx))


