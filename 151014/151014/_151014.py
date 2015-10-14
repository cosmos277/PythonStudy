import re
#pattern=re.compile("d")
#result1=pattern.search("dog")
#result2=pattern.search("dog",1)

#print(result1)
#print(result2)

#str="""sample1.
#sample2.
#sample3."""

#p=re.compile("^.*",re.S) #처음부터 아무거나 들어갈수있다.
#result=p.search(str)
#print(result.group())

#p2=re.compile(".*$",re.S) #처음부터 아무거나 들어갈수있다.
#result2=p2.search(str)
#print(result2.group())

#pattern=re.compile("o[gh]")#og 또는 oh
#result=pattern.fullmatch("dog")
#result2=pattern.fullmatch("ogre")
#result3=pattern.fullmatch("doggie",1,3)
#print(result)
#print(result2)
#print(result3)

#pattern=re.compile("\W+")
#result=pattern.split("words, words, words.")
#result2=pattern.split("words, words, words.",1)

#print(result)
#print(result2)

#pattern=re.compile("x*")
#result=pattern.split('axbc')
#print(result)

#result2=re.sub(r'\WW','','a:b:c, d.')
#print(result2)

#str='<a href="index.html">HERE</a><font size="10">'
#result=re.search(r'href="(.*?)">',str)
#print(result.group(1))

num="123456-1234567"
pattern=re.compile("(\d{6})-(\d{7})")#그냥 match쓰면 자리수 늘리면 안맞음
result=pattern.fullmatch(num) #저틀에 딱맞아야하면 fullmatch사용
print(result.group(1))
print(result.group(2))