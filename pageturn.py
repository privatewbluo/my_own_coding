#! /usr/bin/python3.6
# -*- codeing:UTF-8
# auther wenbluo time:8/26/2020

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def page_turn(url):
    # movies = []
    href = []
    movie_names = []
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    print('Return status', response.status_code)
    parse_info = bs(response.text, 'html.parser')
    for atags in parse_info.find_all('div', attrs={'class': 'hd'}):
        for tag in atags.find_all('a'):
            movie_names.append(tag.find('span').text)
            href.append(tag.get('href'))
            print(tag.find('span').text)
            print(tag.get('href'))

    movies = [href, movie_names]
    return (movies)


if __name__ == '__main__':
    urls = tuple(f'https://movie.douban.com/top250?start={pagenum * 25}&filter=' for pagenum in range(10))
    from time import sleep
    for i in urls:
        page_turn(i)
        sleep(5)
