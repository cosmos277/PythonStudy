#import re

#str="""Window
#Unix
#Linux
#Solaris"""
#p=re.compile('^.+',re.M)
#print(p.findall(str))

#f=re.compile('^.+',re.S)
#result=f.search(str)
#print(result)

#m=re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcolm Reynolds")
#print(m.group('first_name'))
#print(m.groups())

#m2=re.match(r"(\d+)\.?(\d+)?","24")
#print(m2.groups())
#print(m2.groups('10'))

#print(m.groupdict())

#p=re.compile(".+:")
#m=p.search("http://google.com")
#print(m.group())

#p=re.compile(".+(?=:)")
#m=p.search("http://google.com")
#print(m.group())

#import os
#print(os.getcwd())
#os.chdir("C:/")
#print(os.getcwd())

#import glob
#print(glob.glob("*.*"))
#p=re.compile('.*[.](?!bat$|exe$).*$')

#p=re.compile("(?<=abc)def")
#m=p.search('abcdef')
#print(m.group())

#m=re.search('(?<=-)\w+','spam-egg')
#print(m.group())

#email="gmldnjs5197@naremove_thisver.com"
#m=re.search("remove_this",email)
#print(email[m.start()])
#print(email[m.end()])
#result=email[:m.start()]+email[m.end():]
#print(result)

#def displaymatch(match):
#    if match is None:
#        return None
#    print('<Match: %r, groups=%r>' %(match.group(), match.groups()))

#valid=re.compile(r"^[a2-9tjqk]{5}$")
#displaymatch(valid.match("akt5q"))
#displaymatch(valid.match("akt5e"))
#displaymatch(valid.match("akt"))

import re
import urllib.request
with urllib.request.urlopen("http://www.naver.com/") as f:
    str=f.read()
    result=re.search(r"<title>'*+'</title>",str)
    print(result.group())
    