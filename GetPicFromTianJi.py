#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from  bs4 import BeautifulSoup
import  re
import  mysql.connector
import time


page=set()

def get(url):
    # 构造头部
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
    # cookie
    cook = {'afpCT':'1','tmg_utma':'14869497330371380405939741011801','tmg_utmb':'14869497330382663820556115031110',
            'Hm_lvt_0e8d8a461a52de0b1adddeba42c3b860': '1486949733', 'Hm_lpvt_0e8d8a461a52de0b1adddeba42c3b860': '1486949733', 'tmc': '1.86951056.47649493.1486949733587.1486949733587.1486949733587',
            'tma': '86951056.47649493.1486949733587.1486949733587.1486949733587.1', 'tmd': '1.86951056.47649493.1486949733587.', 'fingerprint': '8537385e4de6484461ea20abd463019d',
            'bfd_s': '213341389.517550026027838.1486949735482', '__asc': 'ce504f0e15a351c5cb9475a5177', '__auc': 'ce504f0e15a351c5cb9475a5177',
            'bfd_g': 'ae7402420a012e030000060f000105f258a10d60'}
    data=requests.get(url=url, cookies=cook, headers=headers)
    data.encoding = "gbk"
    web_data=BeautifulSoup(data.text,'lxml')
    re_pic=re.compile('src\=*\.jpg')
    urls=web_data.findAll("img")
    # <img alt="南湘冲击灵魂深处的女神身姿曼妙" src="http://dynamic-image.yesky.com/185x247/uploadImages/2016/321/47/1FCIJ2T15UT3_H.jpg"/>
    for url in urls:
        if 'src' in url.attrs:
            insert(url.attrs['src']);



def insert(text):
    cnn = mysql.connector.connect(user="root", password="123456", host="127.0.0.1", database="mydata")
    cursor=cnn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tianjipic")
    getcount=cursor.fetchall()
    count=getcount[0][0]+1
    insert_sql="INSERT INTO tianjipic (id,url,name ) VALUES(%s,'%s',%s)"%(count,text,"125")
    cursor.execute(insert_sql)
    cnn.commit();
    cnn.close()


if __name__ == "__main__":
    count=20771
    # "http://pic.yesky.com/c/6_20771.shtml"
    for size in range(1,10):
        count+=1
        url = "http://pic.yesky.com/c/6_" + str(count) + ".shtml"
        print(url)
        get(url)
        time.sleep(1)
