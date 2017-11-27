# coding:utf-8

import urllib2
import lxml.html
html = urllib2.urlopen('http://npb.jp/teams/').read() # html 取得
root = lxml.html.fromstring(html)

teams = root.xpath('//a[@class="link_box"]')
for team in teams:
    print(team.text)
