import matplotlib.pyplot as plt
import numpy as np
import random as rm
import scipy.linalg as la

# a=np.array([[4,3,-5],[-4,-5,7],[8,6,-8]])
# print(a)

# (P,L,U)=la.lu(a)
# print(P)
# print(L)
# print(U)
# print(P@L@U)

A = np.array([[4, -1, -1, 0, 0, 0, 0, 0],
                   [-1, 4, 0, 1, 0, 0, 0, 0],
                   [-1, 0, 4, -1, -1, 0, 0, 0],
                   [0, -1, -1, 4, 0, -1, 0, 0],
                   [0, 0, -1, 0, 4, -1, -1, 0],
                   [0, 0, 0, -1, -1, 4, 0, -1],
                   [0, 0, 0, 0, -1, 0, 4, -1],
                   [0, 0, 0, 0, 0, -1, -1, 4]])


(P,L,U)=la.lu(A)
# print(L)
# print(U)
# print(L@U-A)

# b=np.random.randint(47,size=[8,1])

# y=np.linalg.solve(L,b)
# x=np.linalg.solve(U,y)

# print(x)

# Ai=np.linalg.inv(A)
# print(Ai)

C=1
A= np.array([[(1+2*C), -C, 0, 0],
                   [-C, (1+2*C), -C, 0],
                   [0, -C, (1+2*C), -C],
                   [0, 0, -C, (1+2*C)]])

(P,L,U)=la.lu(A)

b=np.array([[10],[15],[15],[10]])

y=np.linalg.solve(L,b)
x=np.linalg.solve(U,y)

print(x)

