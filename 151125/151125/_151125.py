import numpy as np
from matplotlib import pyplot as plt
#data=np.array([[1,2,3],[4,5,6],[7,8,9]])
#data.astype(np.float)
#print(data)
#print(data.T) #전치행렬->여러 행렬별로 실행해보기

#print(np.eye((3))) #단위행렬
#print(np.diag(np.array([1,2,3,4]))) #대각행렬

#print(np.ones((3,2))) #1로 채워진행렬

#print(np.arange(10,1,-1)[:, np.newaxis])#행증가
#print(np.arange(2, 8, dtype=np.float))
#print(np.arange(35).reshape(5,7))

#print(np.linspace(1.,4.,6,endpoint=False))

#data=np.random.randn(16).reshape(4,4)
#print(data)



#data=np.loadtxt('data.txt')
#year,hares,lynxes,carrots=data.T
#print(data)
##plt.plot(year,hares,year,lynxes,year,carrots)
##plt.show()


#print(data[1:4:2,::3])
#x=np.arange(10,1,-1)
#print(x)
#print(x[np.array([3,3,1,8])])
#print(x[np.array([[1,1],[2,3]])])

#y=np.arange(35).reshape(5,7)
#y[np.array([0,2,4])] 
#b=y>20
#print(y[b])

data=np.arange(36).reshape(6,6)
print(data)
mask=np.array(np.array([1,0,1,0,0,1],dtype=bool))
print(mask)
print(data[mask,2])
print(data[3:,mask])
