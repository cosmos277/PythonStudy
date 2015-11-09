from bs4 import BeautifulSoup

#f=open('test.xml')
#xml=f.read()
#soup=BeautifulSoup(xml,"html.parser")
#for node in soup.findAll('node'):
#    print("Node : "+node.string)
#    print("Attr1 : "+node['attr1'])

#f=open('song.xml',encoding='utf-8')
#xml=f.read()
#soup=BeautifulSoup(xml,"html.parser")
#for nodes in soup.test('song'):
#    for node in nodes:
#        print(node.string)
        
#f=open('alcohol.xml',encoding='utf-8')
#xml=f.read()
##soup=BeautifulSoup(xml,"html.parser")
#soup=BeautifulSoup(xml,'lxml')
#for nodes in soup.alcohol('cate1'):
#    #print('Cate1 :'+nodes['tt'])
#    if nodes['tt']=='안주':
#        print(nodes['tt'])
#        for node in nodes('cate2'):
#            print('\tCate2 :'+node['tt'])
#            for item in node('item'):
#                print('\t\t'+item.string)

import json
data={1:'a',2:'b'}
data2=json.dumps(data) #python->json 
data3=json.loads(data2) #json->python 
print(type(data2)) #(str)
print(type(data3)) #(dict)
print(data)
print(data2)
print(data3)

data={1:'우리',2:'나라'} #python data
data2=json.dumps(data,ensure_ascii=False) #json data
print(data2)

s = """
{
"name": "cybaek",
"detail" : { "last": "baek" },
"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""
#beautifulsoup처럼 태그별로 파싱가능
class JsonObject:
    def __init__(self,d):
        self.__dict__=d
data=json.loads(s,object_hook=JsonObject)
print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)