# -*- coding:utf-8 -*- 

#SVD operation
from numpy import *
import numpy as np

np.set_printoptions(precision=1)
np.set_printoptions(suppress=True)

#SVD分解获取3个矩阵

U, Sigma, VT = linalg.svd(  [ [1,1] , [7,7] ])
print  "U = %s" %U
print "sigma = %s" %Sigma
print  "VT = %s" %VT

import svdRec

#分解与重构

def loadExData():
	return [ 
	               [1 ,1 ,1 ,0 ,0 ],
	               [2 ,2 ,2 ,0 ,0 ],
                            [1 ,1 ,1 ,0 ,0 ],
                            [5 ,5 ,5 ,0 ,0 ],
                            [1 ,1 ,0 ,2 ,2 ],
                            [0 ,0 ,0 ,1 ,1]
                         ]

Data = svdRec.loadExData()
U,Sigma,VT = linalg.svd(Data)

Sig3 = mat( [   
	           [Sigma[0] ,0 ,0 ] ,   
	           [0 ,Sigma[1] ,0 ] ,
	           [0 ,0 ,Sigma[2] ] 
	       ] )

Data_Rec = U[: , :3] *Sig3*VT[:3, :]

print  Data_Rec   



