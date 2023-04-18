import numpy as np
import scipy.linalg as la

A=np.random.randint(0,10,size=[5,5])
B=np.random.randint(0,10,size=[5,5])
DA=np.linalg.det(A)
DB=np.linalg.det(B)
C=A+B
DAB=np.linalg.det(C)

print(DA)
print(DB)
print(DAB)
print(DA+DB-DAB)