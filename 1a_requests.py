#! /usr/bin/python3.6
# -*- codeing:UTF-8
# auther wenbluo time:8/26/2020

import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

print(response.text)  ##返回的是html 格式
print(response.status_code)  ## 返回状态码

## 解析html 采用beautifulSoup

parse_info = bs(response.text,'html.parser')

for tags in parse_info.find_all('div',attrs={'class':'hd'}):
    for atag in tags.find_all('a'):
        print(atag.get('href'))
        print(atag.find('span').text)





### xpath 的应用

url2= 'https://movie.douban.com/subject/1292052/'
response2 = requests.get(url2,headers=header)
# xml化处理
selector = lxml.etree.HTML(response2.text)

##电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称: {film_name}')

##电商上映时间

film_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'电影上映时间：{film_date}')

###电影评分

film_score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'电影评分: {film_score}')

mylist = [film_name,film_date,film_score]

movie = pd.DataFrame(mylist)

print(movie)

movie.to_csv('./movie2.csv',encoding='gbk')
movie.to_csv('./movie1.csv', encoding='utf-8', index=False, header=False)

movie.to_csv('./movie1.txt', encoding='utf-8', index=False, header=False)

movie.to_csv('./movie2.txt',encoding='gbk')
