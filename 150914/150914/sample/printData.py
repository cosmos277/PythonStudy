#import printData

#data=["홍길동",["베테랑",["황정민","유아인"],"암살",["전지현","이정재"]],
#       "고길동",["앤트맨","함정"],
#       "이무밍",["오피스","뷰티인사이드"]]
#printData.printData(data)

import os

#help(os.mkdir)
print(os.getcwd())
os.mkdir("sample")
os.chdir(".//sample")
print(os.getcwd())