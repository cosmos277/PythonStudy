print("Hello world")
print("I have %d cats and %d dogs" %(5,6))
print("Here are the numbers! \n"
    "The first is {0:d} The second is {1:4d} ".format(7,8))

##input함수는 String을 반환함-> int로 형변환하여 연산
#salary=int(input("please enter your salary: "))
#bonus=int(input("Please enter your bonus: "))
#payCheck=salary+bonus
#print(payCheck)

data1=5.1234
data2=round(data1,2)
print(data1)
print(data2)
print(type(data1))

##program example1
#print("한글"*3)
#salary=input("월급 : ")
#bonus=input("보너스: ")
#print(type(bonus))

name="greenjoa"
print(name[0])
print(name[-1])
print(name[-2])

info="201311226greenjoa"
sid=info[:9]#0<=info<9
sname=info[9:]
print(sid+" "+sname)

#문자열은 상수로 수정 불가 a[1]=y 안됨
a="pithon"
a=a[:1]+"y"+a[2:]
print(a)

print("I eat %10s apples." %"five")#왼쪽정렬
print("I eat %-10s apples." %"five")#오른쪽정렬

a="Error is %d%%." %98
print(a)

a="I ate{number} apples. so I was sick for {day} days.".format(number=10,day=3)
b="{0:>10}".format("hi")#<좌측정렬 >우측정렬 ^ 가운데 정렬
c="{0:=^10}".format("hi")#공백채우기->가운데 정렬에서 빈공간 '='로채우기
print(c)

#question
#종료할까요? yes YES 소문자로 입력하면 대문자로, 대문자로 입력하면 소문자로 바꾸기

yes=input("종료할까요? ")
print(yes.swapcase())