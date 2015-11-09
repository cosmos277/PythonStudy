import sqlite3
con=sqlite3.connect("test.db")
con.isolation_level=None
cur=con.cursor()
#dropsql='''drop table if exists phonebook;'''
#cur.execute(dropsql)
sql="""create table if not exists phonebook(name text,phoneNum text);"""
cur.execute(sql)

#insertsql='''insert into phonebook values(
#'greenfoa1','010-1111-2222');'''
#cur.execute(insertsql)

#cur.execute("select * from phonebook;")
##for row in cur:
##    print(row)
##    print(row[0])
#print(cur.fetchall())

#name='greenjoa2'
#phoneNumber='010-4926-2742'
#insertsql='''insert into phonebook values(?,?);'''
#cur.execute(insertsql,(name,phoneNumber))


#cur.execute("select * from phonebook;")
#print(cur.fetchone())
#print(cur.fetchall())

#name='greenjoa3'
#phoneNumber='010-8989-7878'
#insertsql='''insert into phonebook values(:inputName,:inputNum);'''
#cur.execute(insertsql, {"inputNum":phoneNumber,"inputName":name})

#cur.execute("select * from phonebook;")
#print(cur.fetchall())

#insertsql='''insert into phonebook values(?,?);'''
#datalist=(('greenjoa4','010-4929-2939'),('greenjoa5','010-2949-2492'))
#cur.executemany(insertsql,datalist)

#cur.execute("select * from phonebook;")
#print(cur.fetchall())

#insertsql='''insert into phonebook values(?,?);'''
#def dataGenerator():
#    datalist=(('greenjoa8','010-8765-4321'),('greenjoa9','010-2839-2424'))
#    for item in datalist:
#        yield item
#cur.executemany(insertsql,dataGenerator())
#con.isolation_level=None


#insertsql="insert into phonebook values('GREENJOA','010-2020-2020');"
#cur.execute(insertsql)

##cur.execute("select * from phonebook order by name desc;")
##print(cur.fetchall())

##cur.execute("select * from phonebook order by name;")
##print(cur.fetchall())

#def OrderFunc(str1,str2):
#    s1=str1.upper()
#    s2=str2.upper()
#    return(s1>s2)-(s1<s2)

#con.create_collation('myordering',OrderFunc)
#cur.execute("select * from phonebook order by name collate myordering;")
#print(cur.fetchall())

#cur.execute("insert into phonebook(phoneNum) values('010-2020-2020');")
#cur.execute("select * from phonebook;")
#print(cur.fetchall())

#cur.execute("select count(*) from phonebook;")
#print(cur.fetchone()[0])

#cur.execute("select count(name) from phonebook")
#print(cur.fetchone()[0])

sql="create table if not exists user(name text,age int);"
cur.execute(sql)


insertsql='''insert into user values(?,?);'''
datalist=(('greenjoa1',21),('greenjoa2',22),('greenjoa3',30),('greenjoa4',46))
cur.executemany(insertsql,datalist)

cur.execute("select name,max(age) from user;")
print(cur.fetchone())
cur.execute("select min(age) from user;")
print(cur.fetchone()[0])

cur.execute("select avg(age) from user;")
print(cur.fetchone()[0])

class Average:
    def __init__(self):
        self.sum=0
        self.cnt=0
    def step(self,value):
        self.sum+=value
        self.cnt+=1
    def finalize(self):
        return self.sum/self.cnt
con.create_aggregate("AVG",1,Average) 
cur.execute("select AVG(age) from user;")
print(cur.fetchone()[0])