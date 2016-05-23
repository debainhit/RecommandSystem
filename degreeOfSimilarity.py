from numpy import *
from numpy import linalg as la

#函数命名首字母不大写，第二个字母大写 都用缩写形式

#simlarity using eulidistance
def eulidSim(inA, inB):
	# 等价的计算欧式距离过程：dist = numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))
	return 1.0 / ( 1.0 + la.norm( inA -inB ) )

#pearson correlation
def pearsSim(inA, inB):
	if len(inA) <3 :return 1.0
	return 0.5 + 0.5*corrcoef( inA,  inB ,rowvar = 0)[0][1]

def cosSim(inA, inB)
            mum = float( inA.T * inB)
            denom = la.norm(inA)*la.norm(inB)
            return 0.5 + 0.5*(num/denom)
