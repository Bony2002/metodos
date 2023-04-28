import numpy as np
import scipy.linalg as la

# A=np.random.randint(0,10,size=[5,5])
# B=np.random.randint(0,10,size=[5,5])
# DA=np.linalg.det(A)
# DB=np.linalg.det(B)
# C=A+B
# DAB=np.linalg.det(C)

# print(DA)
# print(DB)
# print(DAB)
# print(DA+DB-DAB)


# A=np.random.randint(1,10,[4,4])
# b=np.random.randint(1,10,size=[4])

# # print(A)
# # print(b)
# def cramer(A,b):
#     i=0
#     detA=np.linalg.det(A)
#     sol=np.zeros([4])
#     while i < 4:
#         aux=np.copy(A)
#         aux[:,i]=b
#         detaux=np.linalg.det(aux)
#         sol[i]=detaux/detA
#         i+=1
#     return sol

# x=np.linalg.solve(A,b)
# c=cramer(A,b)

# print(x)
# print(c)