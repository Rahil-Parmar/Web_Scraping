import requests
import bs4
import sys
import time
import pandas as pd
header=""
req=requests.get('https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en')
soup=bs4.BeautifulSoup(req.text,'html.parser')
time.sleep(5)
news={'head':[],'url':[],'summary':[],'time':[]}
subnews={'head':[],'url':[],'summary':[],'time':[]}
for x in soup.findAll('div',{'jscontroller':"d0DtYd"}):
    for y in x.findAll('div',class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf"):
        news['summary'].append(y.find('span',class_="xBbh9").text)
        for z in y.find('h3',class_="ipQwMb ekueJc gEATFF RD0gLb"):
            news['head'].append(z.string)
            news['url'].append(z.get('href'))
        n =y.find('div',class_="QmrVtf RD0gLb")
        news['time'].append(n.find('time',class_="WW6dff uQIVzc Sksgp").text)

        for a in y.find('div',class_="SbNwzf").findChildren('article'):
            for b in a.find('h4',class_="ipQwMb ekueJc gEATFF RD0gLb"):
                subnews['head'].append(b.string)
                subnews['url'].append(b.get('href'))
            try:
                subnews['summary'].append(a.find('span',class_="xBbh9").text)
            except AttributeError:
                subnews['summary'].append("")
            k =a.find('div',class_="QmrVtf RD0gLb")
            subnews['time'].append(k.find('time',class_="WW6dff uQIVzc Sksgp").text)
dfnews=pd.DataFrame.from_dict(news)
dfsubnews=pd.DataFrame.from_dict(subnews)
print("1. Main News")
print("2. Sub News")
print("3. Search")
print("Enter Your Choice: ")
n=int(input())
def case(n):
    def one():
        print(dfnews)
    def two():
        print(subnews)
    def three():
        print("Enter a keyword: ")
        s=input()
        for x in soup.findAll('div',{'jscontroller':"d0DtYd"}):
            for y in x.findAll('div',class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf"):
                for z in y.find('h3',class_="ipQwMb ekueJc gEATFF RD0gLb"):
                    if s in z.string:
                        print(z.string)
        for a in y.find('div',class_="SbNwzf").findChildren('article'):
            for b in a.find('h4',class_="ipQwMb ekueJc gEATFF RD0gLb"):
                if s in b.string:
                    print(b.string)
    switcher = {
        1: one,
        2: two,
        3: three,
    }
    func = switcher.get(n, lambda: "Invalid")
    print(func())