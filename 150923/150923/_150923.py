#class HousePark:
#    lastname="박"
#    def __init__(self, name):
#        self.fullname=self.lastname+name
#    def travel(self,where):
#        print("%s, %s 여행을 가다." %(self.fullname,where))

#class HouseKim(HousePark):
#    lastname="김"
#    def __init__(self, name):
#        HousePark.__init__(self,name)
#        self.age=age
#    def travel(self, where):
#        HousePark.travel(self,where)
#        print("%s, %d살에 %s여행 %d일 가네." %(self.fullname,self.age,where,day))

#from abc import ABCMeta, abstractmethod
#class Terran(metaclass=ABCMeta):
#    #생성자
#    def __init__(self, name): 
#        self.name=name
#    @abstractmethod #공통으로 구현해야하는 메소드는 abstract로
#    def attack(self):
#        pass

#class Tank(Terran):
#    def __init__(self,name,damage):
#        super().__init__(name)
#        self.damage=damage
#    def attack(self):
#        print("탱크를 쏩니다.")

#class Marine(Terran):
#    def __init__(self,name,hp):
#        super().__init__(name)
#        self.hp=hp
#    def attack(self):
#        print("총을 쏩니다.")

#def Attack(terran):
#    terran.attack()

#t1=Tank("tank",0)
#t2=Marine("Marine",100)     

#tlist=[Tank("tank1",0),Tank("tank2",50),Marine("Marine1",100)]
#for item in tlist:
#    Attack(item)

##Attack(t1)
##Attack(t2)

class MyList(list):
    name=""
    def __init__(self,name): #list기능은 그대로 갖고 이름을 갖음
        super().__init__([])#list초기화
        self.name=name
    def __str__(self):#오버로딩
        return self.name+":"+super().__str__()

list1=MyList("greenjoa")
list1.append(10)
list1.append(50)
list1.append(60)
list1.append(80)
list1.append(100)

print(list1)
#print(dir(list1))#list1이 갖고있는 멤버들을 나열