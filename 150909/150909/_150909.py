##key:value
dic={'name':'pey','phone':'010449262742','birth':'1118'}
#a={1:'hi'}
#b={'a':[1,2,3]}

#print(dic['name'])
##print(dic)

#a={1:'a'}
#a[2]='b'#데이터추가
#a['name']='pey'
#a[3]=[1,2,3]
#print(a)
#del a['name']#데이터 삭제
#print(a)

#b=dic.keys()
#print(b)

#b=dic.values()
#print(b)

#b=dic.items()
#print(b)

#dic.clear()
#print(dic)

#c={'홍길동':{'베테랑':5.0,'암살':4.5,'뷰티인사이드':3.0},
#   '고길동':{'베테랑':4.0,'암살':5.0,'뷰티인사이드':4.4},
#   '이무밍':{'베테랑':4.2,'암살':3.0,'뷰티인사이드':4.1}}

#print(c['홍길동']['암살'])
#print(c.get('홍길동').get('암살'))#d=~하고 새로운값으로 넘기면 에러??

#answer=input("Would you like express shipping? ")
#if answer.lower()=='yes':
#    print("That will be an extra $10")
#else:
#    print("Have a nice day")

#a=[(1,2),(3,4),(5,6)]
#for (first,last) in a:
#    print(first+last)

#for steps in range(1,10,2):#1에서 10까지 2씩 증가
#    print(steps)

#marks=[90,25,67,45,80]

#a=len(marks)
#print(a)
#for number in range(len(marks)):
#    print(number)

#print()하면 줄바꿈되나 end=""를 하면 줄바꿈이 되지 않는ㄷ
#for i in range(2,10):
#    for j in range(1,10):
#        k=i*j
#        print('{0:d}*{1:d}={2:d}' .format(i,j,k),end=" ")
#    print('')

#for i in range(2,10):
#    for j in range(1,10):
#        k=i*j
#        print('%d*%d=%2d' %(i,j,k),end=" ") 
#    print('')

import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.forward(50)
#        turtle.right(90)

#nSide=20
#for steps in range(nSide):
#    turtle.forward(100)
#    turtle.right(360/nSide)
#    for moresteps in range(nSide):
#        turtle.forward(50)
#        turtle.right(360/nSide)

#for steps in['red','blue','green','black']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)

prompt="""
1. Add
2. Del
3. List
4. Quit

Enter number: """

#print(prompt)
number=0
while number !=4:
    print(prompt,end="")
    number=int(input())