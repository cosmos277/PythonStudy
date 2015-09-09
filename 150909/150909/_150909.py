dic={'name':'yang','phone':'01049262742','birth':'1223'}
#print(dic[2])
#print(dic['birth'])
dic['num']='1'#dic이라는 dictionary에 key는num이고 value는 1103인 값을 추가
#print(dic['birth'])

#b=dic.keys()
#print(b)
#print(dic)
#b=list(dic.keys())

#b=dic.values()

#b=dic.items()
#print(b)
#dic.clear()
#print(b)

#print(dic.get('name'))#없는 경우 none반환

movie={'홍길동':{'베테랑':5.0,'암살':4.5},
       '이무밍':{'베테랑':2.5,'암살':3.0},
       '고길동':{'베테랑':4.0,'암살':4.0}}

#print(movie.items())

##홍길동이 암살에 평점을 얼마 주었는지
#b=movie['홍길동']
#c=b['암살']
#print(c)

#d=movie.get('홍길동')
#print(d.get('암살'))

#print(movie.get('홍길동').get('암살'))

#s1=set([1,1,1])
#print(s1) #<1>
#a=list(s1)
#print(a) #[1]

#answer=input("Would you like express shipping?")
#answer=answer.lower()
#if answer=="yes" : print("That will be an extra $10")
#else: print("Have a nice day")

#a=[(1,2),(3,4),(5,6)]
#for (first, last) in a:
#    print(first+last)

## 1에서 10까지 2씩 띄어서
#for steps in range(1,10,2):
#    print(steps)

#end 옵션에 공백을 넣으면 줄바꿈 안함
#for i in range(2,10):
#    for j in range(1,10):
#        print('%d x %d = %2d '%(i,j,i*j),end=" ") 
#    print('')

import turtle
#nSides=5
#for steps in range(nSides) : #4번동안 움직임
#    turtle.color('blue')
#    turtle.forward(100)
#    turtle.right(360/nSides)
#    for moresteps in range(nSides):
#        turtle.forward(50)
#        turtle.right(360/nSides)

#for steps in ['red','blue','green','black']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)

#counter=0
#while counter<4:
#    turtle.forward(100)
#    turtle.right(90)
#    counter=counter+1

#여러줄을 입력
prompt=""" 
1.Add
2.Del
3.List
4.Quit

Enter number: """

number=0
while number!=4:
    print(prompt, end="")
    number=int(input())