##key:value
dic={'name':'pey','phone':'010449262742','birth':'1118'}
#a={1:'hi'}
#b={'a':[1,2,3]}

#print(dic['name'])
##print(dic)

#a={1:'a'}
#a[2]='b'#�������߰�
#a['name']='pey'
#a[3]=[1,2,3]
#print(a)
#del a['name']#������ ����
#print(a)

#b=dic.keys()
#print(b)

#b=dic.values()
#print(b)

#b=dic.items()
#print(b)

#dic.clear()
#print(dic)

#c={'ȫ�浿':{'���׶�':5.0,'�ϻ�':4.5,'��Ƽ�λ��̵�':3.0},
#   '��浿':{'���׶�':4.0,'�ϻ�':5.0,'��Ƽ�λ��̵�':4.4},
#   '�̹���':{'���׶�':4.2,'�ϻ�':3.0,'��Ƽ�λ��̵�':4.1}}

#print(c['ȫ�浿']['�ϻ�'])
#print(c.get('ȫ�浿').get('�ϻ�'))#d=~�ϰ� ���ο���� �ѱ�� ����??

#answer=input("Would you like express shipping? ")
#if answer.lower()=='yes':
#    print("That will be an extra $10")
#else:
#    print("Have a nice day")

#a=[(1,2),(3,4),(5,6)]
#for (first,last) in a:
#    print(first+last)

#for steps in range(1,10,2):#1���� 10���� 2�� ����
#    print(steps)

#marks=[90,25,67,45,80]

#a=len(marks)
#print(a)
#for number in range(len(marks)):
#    print(number)

#print()�ϸ� �ٹٲ޵ǳ� end=""�� �ϸ� �ٹٲ��� ���� �ʴ¤�
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