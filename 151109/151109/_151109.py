#class Point:
#    def __init__(self,x,y):
#        self.x=x
#        self.y=y
#        def __repr__(self):
#            return "Point(%f,%f)" %(self.x,self.y)
#        def PointAdapter(point):
#            return "%f:%f"%(point.x,point.y)
#        def PointConverter(s):
#            x,y=list(map(float,s.decode().split(":")))
#            return Point(x,y)
## 클래스 이름과 변환 함수 등록 
#sqlite3.register_adapter(Point, PointAdapter) 
## SQL 구문에서 사용할 자료형 이름과 변환 함수 등록 
#sqlite3.register_converter("point", PointConverter) 
#p1 = Point(4,3) 
#p2 = Point(3,4) 
#con1 = sqlite3.connect(":memory:") 
#cur1 = con1.cursor() 
#cur1.execute("create table test(p point);") 
#cur1.execute("insert into test values(?);", (p1,)) 
#cur1.execute("insert into test(p) values(?);", (p2,)) 
#cur1.execute("select p from test") 
#print(cur1.fetchone())


from werkzeug import check_password_hash,generate_password_hash
import sqlite3 as sqlite

def init_db():
    db=sqlite.connect("test.db")
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit()
def get_db():
    db=sqlite.connect("test.db")
    return db

def register():
    print("**** 회원가입 ****\n")
    print("user id : ",end="")
    userid=input()
    print("user name : ",end="")
    username=input()
    print("user passward : ",end="")
    userpw=input()
    
    db=get_db()
    cur=db.cursor()
    cur.execute("select * from user where userid=?",[userid])
    temp=cur.fetchone()

    if(cur.fetchone()!=None):
        print("아이디가 존재합니다.")
        return
    else:
        sql="insert into user(userid,username,userpw) values(?,?,?);"
        cur.execute(sql,[userid,username,generate_password_hash(userpw)])
        db.commit()

    cur.execute("select * from user;")
    print(cur.fetchall())

def login():
    print("**** 로그인 ****\n")
    print("user id : ",end="")
    userid=input()
    print("user passward : ",end="")
    userpw=input()

    db=get_db()
    cur=db.cursor()
    cur.execute("select * from user where userid=?",[userid])
    temp=cur.fetchone()
    if(temp==None):
        print("아이디가 존재하지 않습니다.")
        return
    elif check_password_hash(temp[3],userpw):
        print("로그인 성공")
        return
    else:
        print("비밀번호 체크요함")
        return

#init_db() #처음에만 생성
#register()
login()
