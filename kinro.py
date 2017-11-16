import urllib2
import datetime
from bs4 import BeautifulSoup


def func():
    html = urllib2.urlopen("https://kinro.jointv.jp/lineup")
    soup = BeautifulSoup(html, "lxml")
    today = datetime.date.today()
    nextFriday = today + datetime.timedelta(days = (4 - today.weekday()) % 7)
    strnextFriday = nextFriday.strftime("%Y%m%d")
    a = soup.find_all("a", href = "/lineup/" + strnextFriday)
    tmp = a[0].find("img")
    title = tmp.attrs['alt']
    print(title)

if __name__ == '__main__':
    func()
