#def printMessage():
#    print("Hello world")
#    return

#def main():
#    printMessage()
#    return

#main()

#def main():
#    names=["greenjoa1","greenjoa2","greenjoa3"]
#    newName=input("Enter last guest :")
#    names.append(newName)
#    printNames(names)
#    return
#def printNames(names):
#    for name in names:
#        print(name)
#    return

#main()

#def sum_mul(choice,*args):
#    if choice=="sum":
#        result=0
#        for i in args:
#            resut=result+i
#    elif choice=="mul":
#        result=1
#        for i in args:
#            result=result*i
#        return
#    return
#resul=sum_mul("sum",1,2,3,4,5)

#def sum_mul(a,b):
#    return a+b,a*b
#answer=sum_mul(10,30)
#print(answer) #튜플로 출력됨 (40,300)

##변수에 담고싶다면
#sum,mul=sum_mul(3,4)
#print(sum,mul)

#coding:cp949
#인코딩 모드를 cp949로 보여지는데이타를 바꾸는것이 아니라 저장하는것을 바꾸려면

def printData(data,level=0):
    for item in data:
        if isinstance(item,list):
            printData(item,level+1)#재귀함수를 이용하여 계속 list가 반복되어도 출력
        else:
            for i in range(level):
                print("   ",end="")
            print(item)

    return


data=["홍길동",["베테랑",["황정민","유아인"],"암살",["전지현","이정재"]],
       "고길동",["앤트맨","함정"],
       "이무밍",["오피스","뷰티인사이드"]]

printData(data)