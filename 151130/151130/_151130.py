import numpy as np
from matplotlib import pyplot as plt

##행렬의 연산
#list=[1,2,3,4]
#print(list*2)
#data=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(data+2)
#print(data*2)
#print(data*data)#각 원소끼리 곱->행렬의 곱이 아니다
#print(data.dot(data))#행렬의 크기가 맞아야한다 

##비교연산
#a=np.array([1,2,3,4])
#b=np.array([4,2,2,4])
#print(a==b)
#print(a>b) #원소에 대한 비교
#print(np.array_equal(a,b)) #array에 대한 비교

##논리연산
#a=np.array([1,1,0,0],dtype=bool)
#b=np.array([1,0,1,0],dtype=bool)
#print(np.logical_or(a,b))
#print(np.all([True,True,False]))#안의 원소가 다 true여야 true
#print(np.any([True,True,False]))

##초월함수
#a=np.arange(5)+1
#print(np.sin(a))
#print(np.log(a))

##전이행렬
#a=np.triu(np.ones((3,3)),-1)
#print(a)
#print(a.T)

##Sum
#x=np.array([1,2,3,4])
#print(np.sum(x))
#print(x.sum())

#x=np.array([[1,1],[2,2]])
#print(x.sum()) #모든 원소의 함
#print(x.sum(axis=0))
#print(x.sum(axis=1))

##최대,최소
#x=np.array([1,3,2])
#print(x.min()) #최소값
#print(x.argmin()) #최소값의 인덱스값

##논리연산->배열 비교할 때 주로 사용
#a = np.zeros((100,100))
#print(np.any(a!=0))
#np.all(a==a)

##통계
#x=np.array([1,2,3,1])
#y=np.array([[1,3,4],[5,6,1]])
#print(x.mean()) #평균
#print(np.median(x)) #중간값
#print(np.median(y,axis=-1))
#print(x.std())

##응용
#data=np.loadtxt('data.txt')
#year,hares,lynxes,carrots=data.T
##plt.plot(year,hares,year,lynxes,year,carrots)
##plt.show()

#x=np.array([hares,lynxes,carrots])
##print(x.sum(axis=0)/21) #전체 개체의 년도별 평균
##print(x.sum(axis=1)/21) #각 개체별 전체평균
##y=x.sum(axis=1)/21

#print(hares.mean()) #평균
#print(lynxes.mean())
#print(carrots.mean())

#print(hares.std()) #표준편차
#print(lynxes.std())
#print(carrots.std())

#print(int(year[hares.argmax()])) #토끼의 최대 개체수 년도
#print(int(year[lynxes.argmax()])) #시라소니의 최대 개체수 년도
#print(int(year[carrots.argmax()])) #당근의 최대 개체수 년도

#broadcasting
#data=np.arange(50).reshape(5,10)
#print(data)

data=np.array([[0,10,20,30,40,50]]).T
print(data.shape)
print(data+[0,1,2,3,4,5])