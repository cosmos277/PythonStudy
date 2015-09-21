#class Service:
#    secret="영구는 배꼽이 두 개다." #클래스 변수
#    def sum(self,a,b):
#        result=a+b
#        print("%s + %s = %s 입니다." %(a,b,result))
#        return
   
#    pey=Service()
#    print(pey.secret)
#    #pey2=Service()

#    pey.sum(1,1) #바운드된 메소드 호출에서는 self를 넘길 필요가 없지만
#    #Service.sum(pey2,1,1) #언바운드된 메소드 호출에서는 객체를 넘겨주어야한다.

class Movie:
    '''영화 클래스입니다'''
    count=0
    title="암살"
    director="최동훈"
    def __init__(self,title,director):
        self.title=title
        self.director=director
        Movie.count+=1
        print(self.title+"생성자 호출")
        
    def __del__(self):
        print(self.title+"소멸자 호출")

    def showInfo(self):
        print(self.title+" "+self.director)
    
    @staticmethod #decorater
    def showCount1(): #클래스정보가 들어오지 않음
        print(Movie.count)
    @classmethod
    def showCount2(cls):
        print(cls.count) #Movie라는 클래스 정보가 없이 cls로

#m1=Movie("암살","홍길동") #Movie.__init__(m1,"암살","홍길동")
#m2=Movie("영화1","고길동")

#print(m1.title)
#m1.title="암살2"
#print(m1.title)
#m2.__class__.title="베테랑"

#print(m1.title, m2.title)

#print(m1.__doc__)




#m1=Movie("암살1","홍길동1")
#m2=Movie("암살2","홍길동2")
#m3=Movie("암살3","홍길동3")

#m4=Movie("암살4","홍길동4")
#print(type(m4))
#m4=m3 #대입연산하면 같은 주소를 가리키게 된다(얕은복사)
##깊은복사 하고싶으면 따로..
#print(id(m4))#id는 주소값
#print(id(m3))
#m4.showInfo()


#m1=Movie("a","b")
#m2=Movie("c","d")
#print(m1.count)
#print(m2.count)

#m1.__class__.count+=1
#print(m1.count)

m1=Movie("a","b")
m2=Movie("c","d")
m3=Movie("e","f")
m4=Movie("g","h")
m5=Movie("i","j")

Movie.showCount1()
Movie.showCount2()
