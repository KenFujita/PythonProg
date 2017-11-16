import urllib2
import lxml.html
import requests
from selenium import webdriver

tgt_html = 'http://news.tv-asahi.co.jp/news_politics/articles/000041338.html'
driver = webdriver.PhantomJS()
driver.get(tgt_html)
dom = lxml.html.fromstring(driver.page_source)
linkList = dom.cssselect('#relatedNews a')

for w in linkList:
    print w.text
