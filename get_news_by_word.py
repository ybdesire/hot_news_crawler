#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd


__author__ = 'ybdesire@gmail.com'
__date__ = '2019-01-21'
__version_info__ = (0, 0, 1)
__version__ = '.'.join(str(i) for i in __version_info__)



if __name__ == '__main__':
    key_word = '编程'
    url = 'http://news.baidu.com/ns?cl=2&rn=50&tn=news&word={0}'.format(key_word)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    response = requests.get(url,headers = headers)
    html_doc = response.content 
    #print(html_doc)
    soup = BeautifulSoup( html_doc, 'html.parser')
    # get all content at tag a
    pids = soup.findAll('a')
    result = []
    for pid in pids:
        p = pid.attrs
        if('target' in p and p['target']=='_blank' and 'data-click' in p):
            if('百度快照' not in pid.contents[0]):
                slist = []
                for x in pid.contents:
                    slist.append(str(x))
                s = ''.join(slist)
                s = s.replace('\n','').replace(' ','').replace('<em>','').replace('</em>','')
                result.append(s)
                
    # save to excel
    d = {'titles': result[:100]}
    df = pd.DataFrame(data=d)
    from pandas import ExcelWriter

    writer = ExcelWriter('hot_news.xlsx')
    df.to_excel(writer,'Sheet1')
    writer.save()

            
                
