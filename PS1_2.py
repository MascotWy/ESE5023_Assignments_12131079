# -*- coding: utf-8 -*-
import numpy as np
def Matrix_multip (M1,M2):
   S=np.zeros((5,5))
   for i in range(0,5):
       for j in range(0,5):
           for m in range(0,10):
               S[i,j]+=M1[i,m]*M2[m,j]
   print(M1,M2,S)

M1=np.random.randint(0,50,(5,10))
M2=np.random.randint(0,50,(10,5))
Matrix_multip(M1,M2)