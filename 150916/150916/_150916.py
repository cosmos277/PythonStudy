#fileName="greenjoa.txt"
#with open(fileName,"r") as myFile:
#    #myFile.write("201311226 양희원\n")
#    #myFile.write("201312345 홍길동\n")
#    #myFile.write("201311247 이무밍\n")

#    fileContents=myFile.read()
#    print(fileContents)

#with open(fileName,"r")as myFile:
#    while True:
#        content=myFile.readline()
#        if not content:
#            break
#        print(content)


import pickle #dump라는 함수를 이용하여 file에 저장할수있음, read 얘는 r/w가 binary이므로 b가 붙어서 wb,rb형태로 사용

fileName="파일입출력예제2.txt"
fileName2="Monica2.txt"
roles=[] #리스트하나 생성

with open(fileName,"r") as myFile, open(fileName2,"wb") as monica:    
    for content in myFile:
        (role,etc)=content.strip().split(":",1)#max split조건을 넣어서 :가 두번이상 나오는것을 1개로 방지한다
        roles.append(role)
        
        #if(role=="Monica"):
        #    monica.write(etc)
        #    monica.write("\n")
#print(roles)
    pickle.dump(roles,monica)
    
with open(fileName2,"rb") as monica:    
    result=pickle.load(monica)
    print(result)
    #메모리에서 사용한 구조 그대로 출력할수있다는 점이 중요