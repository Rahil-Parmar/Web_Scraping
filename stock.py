import requests
import bs4
import time
import numpy as np

req=requests.get("https://www.moneycontrol.com/stocks/marketstats/indexcomp.php")
soup=bs4.BeautifulSoup(req.text,'html.parser')
now=time.time()
future=now+1200
n=len(soup.findAll('tr'))-1
arr=np.full((n,2),0.0)
old={'company':[],'industry':[],'lPrice':[],'change':[],'pChange':[],'Market Capital':[]}
new={'company':[],'industry':[],'lPrice':[],'change':[],'pChange':[],'Market Capital':[]}
for a in soup.findAll('tr'):
        i=0
        for b in soup.findAll('td',class_="brdrgtgry"):
            if i==0:
                x=b.find('a',class_="bl_12")
                new['company'].append(b.find('a',class_="bl_12").text)
                i=1
            elif i==1:
                new['industry'].append(b.find('a',class_="bl_12").text)
                i=2
            elif i==2:
                new['lPrice'].append(b.text)
                i=3
            elif i==3:
                new['change'].append(b.text)
                i=4
            elif i==4:
                new['pChange'].append(b.text)
                i=5
            elif i==5:
                new['Market Capital'].append(b.text)
old['company']=new['company']
old['industry']=new['industry']
old['lPrice']=new['lPrice']
old['change']=new['change']
old['pChange']=new['pChange']
old['Market Capital']=new['Market Capital']  
for i in range(n):
    arr[i][0]= old['pChange'][i]
    arr[i][1]=new['pChange'][i]   
while future-now > 0:
    cref=0
    for a in soup.findAll('tr'):
        i=0
        for b in soup.findAll('td',class_="brdrgtgry"):
            if i==0:
                x=b.find('a',class_="bl_12")
                new['company'].append(b.find('a',class_="bl_12").text)
                i=1
            elif i==1:
                new['industry'].append(b.find('a',class_="bl_12").text)
                i=2
            elif i==2:
                new['lPrice'].append(b.text)
                i=3
            elif i==3:
                new['change'].append(b.text)
                i=4
            elif i==4:
                new['pChange'].append(b.text)
                i=5
            elif i==5:
                new['Market Capital'].append(b.text)
    for z in range(len(new['pChange'])):
        print(str(new['company'][z])+"    "+str(new['industry'][z])+"    "+str(old['lPrice'])+"    "+str(new['lPrice'])+"    "+str(new['pChange']))
    j=0
    if cref==4:
        for z in range(len(new['pChange'])):
            if new['pChange'][z]>=2:
                if j==0:
                    print("The price changes by more than 2'%' for ")
                print(str(new['company'][z])+"    "+str(new['industry'][z])+"    "+str(new['lPrice'])+"    "+str(new[''])+"    "+str(new['pChange']))
            arr[z][0]=arr[z][1]
        cref=0
    old['company']=new['company']
    old['industry']=new['industry']
    old['lPrice']=new['lPrice']
    old['change']=new['change']
    old['pChange']=new['pChange']
    old['Market Capital']=new['Market Capital'] 
    for h in range(len(new['pChange'])):
        arr[z][1]=new['pChange'][h]
    time.sleep(30)
    now=time.time()
    cref=cref+1
