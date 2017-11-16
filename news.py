import lxml.html
import requests

target_url = 'http://news.tv-asahi.co.jp/news_politics/articles/000041338.html'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)

print(root.cssselect('#news_body > p')[0].text_content())
