#print(all([1,2,3])) #True
#print(all([0,1,1])) #False

#num=[1,2,3,4]
##print(dir(num))

#print(divmod(7,3))

#data=list(enumerate(num)) #(순서,실제값)
#print(data)

#print(eval("1+2"))
#print(eval("divmod(4,3)"))


#def positive(l):
#    return l%2==0
#print(list(filter(positive,[1,-3,2,0,-5,6])))

#a=3
#print(id(3))
#print(id(a))

#print(isinstance(10,int))

#sum1=lambda a,b :a+b
#print(sum1(3,4))

#def sum2(a,b):
#    return a+b
#print(sum2(3,4))

#l=[lambda a,b:a+b, lambda a,b:a*b]
#a=l[0](3,4)
#b=l[1](3,4)

#print(a)
#print(b)

#print(list(filter(lambda x:x%2==0,[1,-3,2,0,-5,6])))

#a=[1,2,3]
#b=list(a) #새로만들어주는것이므로 id다르다
#c=a #참조이므로 id같다

#print(id(a))
#print(id(b))
#print(id(c))


#a=list(map(lambda a:a*2,[1,2,3,4]))
#b=map(lambda a:a*2,[1,2,3,4])
#print(a) 
#print(b) 

#a=max([1,2,3]) #3
#b=min("python") #h
#print(a)
#print(b) 

#a=eval(repr("hi".upper()))
##b=eval(str("hi".upper())) #에러
#print(a)

#a=sorted([3,1,2])
#print(a)
#b=sorted("zero")
#c=sorted(['c','b','a'])
#print(b)
#print(c)

#d=[1,3,5,3,7,8,9]
#d.sort()
#print(d)

#a=list(zip([1,2,3],[4,5,6],[7,8,9]))
#print(a)

data={
    '홍길동':[80,70,60,92],
    '김길동':[24,35,18,10],
    '고길동':[10,20,8,5]
    }

#print(type(data))

#b=data.values()
#print(b)

#a=data['홍길동']
#a.sort()
#b=data['김길동']
#b.sort()
#c=data['고길동']
#c.sort()

for i in data:
    data[i].sort()

print(data['홍길동']) #[60,70,80,92]

data=sorted(data.items())
print(data)