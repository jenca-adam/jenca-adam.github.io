print('importing modules')
print('importing fpdf.FPDF')
from fpdf import FPDF
print('importing pdfplumber')
import pdfplumber
print('importing os')
import os
print('importing httplib2')
import httplib2
print('importing bs4')
from bs4 import BeautifulSoup as bs
print('importing random')
import random
print('importing re')
import re
class PageDoesNotExistError(ValueError):pass
class ArXivPage:
    def __init__(self,id):
        self._h=httplib2.Http('.cache')
        self.arxid=id
    def getpdf(self):
        print(f'downlading arXiv page: {self.arxid}')
        url=f'http://arxiv.org/pdf/{self.arxid}'
        resp,cont=self._h.request(url)
        if resp.status==404:
            raise PageDoesNotExistError('check your id!')   
        print('writing file')
        with open(f'{self.arxid}.pdf','wb')as f:
            f.write(cont)
        return f'{self.arxid}.pdf'
def extract_text(id):
    error=''
    print('creating arxiv page object')
    arxpage=ArXivPage(id)
    print('extracting pdf')
    pdf=arxpage.getpdf()
    try:
        a=pdfplumber.open(pdf)
    except:
        os.remove()
        error=ValueError('probably not a pdf file')
    if error:
        raise error
    print('selecting pages')
    p=a.pages
    tx=''
    print('iterating through pages')
    pin=1
    for i in p:
        print(f'extracting text from page {pin}') 
        tx+='\n'+i.extract_text()
        pin+=1
    print('deleting file')
    os.remove(pdf)
    return tx
def randompages():
    q=['math-ph','quantum','neumann','algebra','COVID-19','quant-ph']
    qq=random.choice(q)
    print('selected search term '+qq)
    start=random.randrange(100)
    
    size=100
    url=f'http://arxiv.org/search?query={qq}&searchtype=all&abstract=hide&start={start}&size={size}'
    print(f'requesting {url}') 
    r,c=httplib2.Http('.cache').request(url)  
    print('parsing html')
    soup=bs(c,'html.parser')
    results=soup.find_all('li',class_='arxiv-result')
    res=[r.div.p.a['href'] for r in results]
    print('getting ids from results')
    pattern='https?://arxiv.org/abs/(\S*)$'
    res=[re.search(pattern,r).groups()[0] for r in res]
    print(f'{len(res)} results')
    return res
def all_text():
    return [extract_text(i) for i in randompages()]
    
        
        
        
