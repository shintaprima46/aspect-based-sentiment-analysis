
# coding: utf-8

# code from https://stackoverflow.com/questions/54554261/selenium-unable-to-locate-app-id-title-element-when-trying-to-load-google-play

#load webdriver function from selenium
from selenium import webdriver
from time import sleep
import bs4
import pandas as pd
import requests
from selenium.webdriver.common.keys import Keys
import time

# Change this number to get more or less reviews
x = 1000

link = "https://play.google.com/store/apps/details?id=com.tokopedia.tkpd&showAllReviews=true" #link of review source

driver = webdriver.Chrome('C:/WinPython_64bit/notebooks/Google-Play-Store-Review-Extractor-master/chromedriver.exe')
driver.get(link + '&showAllReviews=true')

num_clicks = 0
num_scrolls = 0
while num_clicks <= x and num_scrolls <= x*5:
    try:
        show_more = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/content/span')
        show_more.click()
        num_clicks += 1

    except:
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        num_scrolls +=1
        time.sleep(2)

soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
h2 = soup.find_all('h2')

results_df = pd.DataFrame()
for ele in h2:
    if ele.text == 'Reviews':
        c_wiz = ele.parent.parent.find_all('c-wiz')
        for sibling in c_wiz[0].next_siblings:
            try:
                #print (sibling)
                comment_shift = 0
                spans = sibling.find_all('span')
                for user_block in range(0,len(spans)):
                    i = user_block *10
                    name = spans[i+0+comment_shift].text
                    try:
                        rating = spans[i+1+comment_shift].div.next_element['aria-label']
                        rating = str(''.join(filter(str.isdigit, rating)))
                    except:
                        comment_shift += 2
                        continue
                    date = spans[i+2+comment_shift].text
                    review = spans[i+8+comment_shift].text
                    print ('Name: %s\nRating: %s\nDate: %s\nReview: %s\n' %(name, rating, date, review))
                    temp_df = pd.DataFrame([[date, rating, name, review]], columns = ['Date','Rating','User','Review'])

                    results_df = results_df.append(temp_df)
            except:
                continue

results_df = results_df.reset_index(drop=True)
results_df.to_csv('C:/WinPython_64bit/notebooks/Google-Play-Store-Review-Extractor-master/review_tokped.csv', index=False)

driver.close()
