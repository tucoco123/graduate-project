#encoding:utf-8
import requests
import json
import csv
import time
from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#打開json檔（讀檔）
jsonData = open('output.json','r')
#打開用instagram-crawler爬好的表格
csvfile = open('csv_output.csv', 'w',newline='')

#設定字典
fieldnames = ['index', 'userId']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#將設定的字典寫上
writer.writeheader()


with open('output.json','r')as f:
    #打開Firefox驅動程式geckodriver（需下載）
    #因為系統一直讀不到，所以設了路徑
  dirver = webdriver.Firefox(executable_path=r'/Users/tucoco123/Desktop/geckodriver')
  source = f.read()#讀json檔
  data = json.loads(source)#編碼
  for i in range(len(data)):
    print (i)
    try:#出現error跳過，讓迴圈可以跑完
        url = data[i]['key']
        #找標籤爬蟲
        dirver.get(url)
        html_text = dirver.page_source
        soup = BeautifulSoup(html_text, 'html.parser')
        article = soup.find('div',attrs={'class':'KlCQn EtaWk'})
        if article != None:
          href = article.findAll('a',attrs={'class':'FPmhX notranslate TlrDj'})
          writer.writerow({  'index' : i  ,  'userId' : str(href[0]['title']) })
        print(str(href[0]['title']))
    except:#網頁已失效的印except
        writer.writerow("except")
        print("except")
        pass
    continue
#    time.sleep(10)
#    dirver.quit()

  
