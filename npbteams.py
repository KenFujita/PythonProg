# -*- coding: UTF-8 -*-

import urllib.request
import lxml.html
html = urllib.request.urlopen('http://npb.jp/teams/').read() # html 取得
root = lxml.html.fromstring(html)

teams = root.xpath('//a[@class="link_box"]')
hp = root.xpath('//a[@class="link_box"]/@href')
for i in range(12):
    print(teams[i].text+"\t"+"\t"+"\t"+hp[i])
