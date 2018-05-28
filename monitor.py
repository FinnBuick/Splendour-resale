# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

import pyautogui

import webbrowser

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),
count = 0
while True:
    # set the url as Moshtix,
    url = "http://www.moshtix.com.au/v2/event/splendour-in-the-grass-2018/103360"
    # set the headers like we are a browser,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")


    # if the number of times the word "Google" occurs on the page is less than 1,
    if soup.find(class_="col-quantity col-quantity-216690").find('select') is None:
        # wait 60 seconds,
        print("Refresh #" + str(count))
        count+=1
        time.sleep(1)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        pyautogui.click()
        print(time.asctime())

        break