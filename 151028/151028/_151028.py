#import urllib.request
#with urllib.request.urlopen('http://www.python.org/') as f:
#    print(f.read())
#    print(f.read(300)) #300 byte
#    print(f.read(300).decode("utf-8")) #encoding mode utf-8

#from urllib.parse import urlparse
#result = urlparse('http://search.naver.com/search.naver?where=nexearch&query=urllib.parse&sm=top_hty&fbm=1&ie=utf8')
#print(result)
#print(result.scheme)
#print(result.geturl())


#import os
#os.system("python -m pip install beautifulsoup4")

#from bs4 import BeautifulSoup
#html_doc= """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""

#soup=BeautifulSoup(html_doc,"html.parser")
#print(soup.html.head.title.prettify())
#print(soup.a.prettify())
#print(soup.html.head.title.string)
#print(soup('a',{'class':'sister'}))
#print(soup('a')[0].previous)
#print(soup.find('a')['href'])
#print(soup.find_all(id='link3'))
#print(soup.find_all(class_='sister'))

#coding:cp949

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
import urllib
import webbrowser

#url= "http://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu"
#data=urlopen(url)
#soup=BeautifulSoup(data,'html.parser')
#cartoons=soup.find_all('td',{'class':'title'})
#print(soup.title.string)
#for i in range(len(cartoons)):
#    title=cartoons[i].find('a').string
#    ref=cartoons[i].find('a')['href']
#    tempurl=urljoin(url,ref)
#    print(title," ",tempurl)
#print(ref)
#webbrowser.open_new(tempurl)   

class crawler:
    def crawl(self,pages,depth=2):
        for i in range(depth):
            newpage=set()
            for page in pages:
                print(page)
                try:
                    c=urllib.request.urlopen(page)
                except:
                    print("Could not open %s" %page)
                    continue
                soup=BeautifulSoup(c.read(),from_encoding="utf-8")
                print("Found %s" %page)
            links=soup('a')
            for link in links:
                if('href' in dict(link.attrs)):
                    url=urllib.parse.urljoin(page,link['href'])
                    if url.find("'")!=-1:continue
                    url=url.split("#")[0]
                    if url[0:4]=="http":
                        newpage.add(url)
            pages=newpage

pagelist=['http://www.naver.com']
crawler=crawler()
crawler.crawl(pagelist)
#c=urllib.request.urlopen('http://www.naver.com')
