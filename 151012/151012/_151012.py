import sys
##print(sys.path)
import os

#os.system("python test.py a b c")
#print(sys.path)

#class Student:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def show(self):
#        print(self.name,":",self.age)

#s1=Student("yang","22")
#s1.show()
#s2=Student("hui","5")

#import pickle

#f=open("test.txt","wb")
#pickle.dump(s1,f)
#f.close()

#print(os.environ)
#print(os.getcwd())
#path=os.getcwd()
#os.chdir("..")
#print(os.getcwd())


#os.system("dir")

#f=os.popen("dir")
#print(f.read())

#for(path,dir,files) in os.walk(".."):
#    for filename in files:
#        print(filename)

#print(list(os.walk("..")))

#import shutil
#shutil.copy("test.txt","dst.txt")



##
#import pickle
#import shutil
##os.mkdir("./sample")
#destination = "./sample/"

#for(path,dir,files) in os.walk("."):
#    for filename in files:
#        #print(filename)
#        (name,st)=filename.strip().split(".")
#        #print(st)
#        if(st=="txt"):
#            print(filename)
#            shutil.copy(filename,destination)
            
#    #if filename

#import shutil
#import os
#source = os.listdir(".")
#destination = "./sample/"
#for files in source:
#    if files.endswith(".txt"):
#        shutil.copy(files,destination)


#print(os.path.dirname("c:\python34\python.exe"))
#print(os.path.expanduser("~\\python.exe"))


#print(os.path.split("c:\python34\python.exe"))
#print(os.path.splitdrive('C:\Python34\python.exe'))

#import glob

#path=os.getcwd()
#print(glob.glob('*.txt'))

#for i in glob.iglob('*'):
#    print(i)

#import glob,os.path

#ndir=nfile=0
#def traverse(dir,depth):
#    global ndir,nfile
#    for obj in glob.glob(dir+'/*'):
#        if depth==0:
#            prefix='|--'
#        else:
#            prefix='|'+' '*depth+'|--'
#        if os.path.isdir(obj):
#            ndir+=1
#            print(prefix+os.path.basename(obj))
#            traverse(obj,depth+1)
#        elif os.path.isfile(obj):
#            nfile+=1
#            print(prefix+os.path.basename(obj))
#        else:
#            print(prefix+'unknown object:',obj)

#if __name__ =='__main__':
#    traverse('..',0)
#    print('\n',ndir,'directories',nfile,'files')

#import os.path

#import tempfile
#with tempfile.TemporaryFile('w+',delete=False) as fp:
#    fp.writelines('Hello world!')
#    fp.seek(0)
#    data=fp.read()
#    tempname=fp.name
#    print(tempname)
#    print(os.path.exists(tempname))
#    print(data)
#print(os.path.exists(tempname))

#import time
#t1=time.time()
#time.sleep(5)
#t2=time.time()
#spendtime=t2-t1
#print(spendtime)

#import time
#time1=time.ctime(1234567)
#t=time.strptime(time1)
#print(t)

#print(time1)

#import calendar
##calendar.calendar(2000)
#calendar.prcal(2000)

#print(calendar.weekday(1994,12,23))
#print(calendar.monthrange(2015,10))


import random
#num=random.randrange(0,101,2)
#print(num)
#list=[1,2,3,4,5,6,7,8,9]
#a=random.choice(list)
#print(a)
#random.shuffle(list)
#print(list)

#list=list2=[]
#for i in range(100):
#    list.append(random.randrange(1000))
#print(list)
#random.shuffle(list)
#list2=random.sample(list,10)
#print(list2)

#data=[('Red',3),('Blue',2),('Yellow',1),('Green',4)]
#datalist=[]
##for val,cnt in data:
##    for i in range(cnt):
##        datalist.append(val)
##print(datalist)

#datalist=[val for val, cnt in data for i in range(cnt)]
#print(datalist)

import webbrowser
url='http://google.com'
webbrowser.open_new_tab(url)