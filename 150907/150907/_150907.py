#a=[]
#b=[1,2,3]
#c=["Life","is","too","short"]
#d=[1,2,"Life","is"]
#e=[1,2,["Life","is"]]
#print(e[2][0])

#data=['a','b','c',['abcd','efg']]
#print(data[0])
#print(data[-1])
#print(data[3][1])

#print(b+c)
#print(b*3)

#f=b+c
#print(f)

#guests=['a','b','c','d']
##guests[0]='greenjoa'
##guests[1]=['greenjoa1','greenjoa2']
##guests[1:2]=['greenjoa1','greenjoa2']#1보다크거나같고2보다 작은=guset[1]
#print(guests)

#guests.insert(2,'e')
#guests.append('greenjoa2')

#id=['gmldnjs5197','yahoo5197','hw5197']
#id.insert(1,['1234','양희원','01049262742'])
#id.insert(3,['5678','이무명','01012345678'])
#id.insert(5,['90','홍길동','01067574747'])
#print(id)

#range(6)은 0~5까지->index번호를 의미
#guests=['a','b','c','d']
#for steps in range(6):
#    print(steps)

#data2=range(4)
#print(data2)

#nEntries=len(id)
#for steps in range(nEntries):
#    print(id[steps])

#for init in id:
#    print(init)

scores=[85,62,63,45,90,101,2,59,22,13,77]
#print(scores)
scores.sort() #숫자만
scores.reverse()
top5 = scores[0:5]
print(top5)

#for steps in range(6):
#    if isinstance(steps,list):
#        for step in steps:
#            print(step)    
#    else :
#        print(steps)

num=top5.pop()
print(num)
num=top5.pop(2)
print(num)
print(top5)

#extend와 append의 차이
#extend:list에 포함시켜준다, append:그냥 붙여준다
top5.extend([50,60])
print(top5)
top5.append([50,60])
print(top5)

t1=()
t2=(1,)
t3=(1)
t4=(1,2,3)
t5=1,2,3
#t4와 t5는 같다
t6=('a','b',('ab','cd'))

print(t1,t2,t3,t4,t5,t6)