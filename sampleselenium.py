from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re

options = Options()
# バックグラウンドで動かす
options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver",options=options)
driver.get("https://www.anikore.jp/anime_review/3772/")
print("get web source")
time.sleep(5)
# 画面外の要素にアクセスするため
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 隠されている要素を表示する
driver.find_element_by_link_text("ネタバレレビューを読む").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_link_text("もっと見る").click()

print("get review titles")
i=0
elem_title_list = []
elem_kutikomi_list = []
elem_score_list = []
while True:
    try:
        # 「次の30件を表示」をクリック
        driver.find_element_by_xpath("//div[@class='l-animeDetailReviewMoreBtn']").click()
        #driver.find_element_by_link_text("ネタバレレビューを読む").click()
        #driver.find_element_by_link_text("もっと見る").click()
        # タイトルと本文を抽出
        elem_title_list.extend(driver.find_elements_by_xpath("//h3[@class='m-animeDetailReviewUnit_userText_title']/a"))
        elem_kutikomi_list.extend(driver.find_elements_by_xpath("//p[@class='m-animeDetailReviewUnit_userText_content ateval_description']"))
        #elem_score_list.extend(driver.find_elements_by_xpath("//p[@class='m-animeDetailReviewUnit_userText_pointLane']/strong"))

        elem_title_list = sorted(set(elem_title_list),key=elem_title_list.index)
        elem_kutikomi_list = sorted(set(elem_kutikomi_list),key=elem_kutikomi_list.index)
        time.sleep(5)
        print("clicked: {}, more btn clicked".format(str(i)))
        i+=1
    except:
        print("more btn is none")
        break

print("sum of title: {}, sum of con: {}".format(len(elem_title_list),len(elem_kutikomi_list)))
context_data = []
for title,kutikomi in zip(elem_title_list,elem_kutikomi_list):
    # get_attribute()でないと、display none になっている要素の中身が取得できない（selenium側で無いものとして扱われるため）
    context_data.append([title.get_attribute("textContent").replace(" ",""),kutikomi.get_attribute("textContent").replace(" ","")])
    #print("title: {}, context: {}".format(title.get_attribute("textContent"),kutikomi.get_attribute("textContent")))
df_review = pd.DataFrame(context_data,columns=['title','review'])
df_review.to_csv("gup_review.csv")
print("done!!")

driver.close()
