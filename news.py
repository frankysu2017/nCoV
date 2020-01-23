#!/usr/bin/env python3
# coding=utf-8
# news.py

import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
import cpca

def get_news():
    nCov_url = r'https://3g.dxy.cn/newh5/view/pneumonia?from=timeline&isappinstalled=0'
    r = requests.get(nCov_url)
    r.encoding = 'utf8'
    b = BeautifulSoup(r.text, features="html.parser")
    l = b.find_all('div', attrs={'class': 'block___wqUAz'})
    for item in l:
        left, right = list(item.children)[0:2]
        title = (list(right.p.strings)[-1].strip().replace(' ', ''))
        publish_time = parse(item.div.get_text().split('前')[-1].replace('月', '-').replace('日', ' '))
        content = right.find_all('p', attrs={'class': 'topicContent___1KVfy'})[0].string.replace(' ', '')
        print(publish_time, title)
        print(cpca.transform([title])[['市', '省']])
        print()
        #print(content)


if __name__ == '__main__':
    get_news()
