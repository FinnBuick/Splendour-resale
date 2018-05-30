# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

#import pyautogui
import winsound
import webbrowser

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),
count = 0
# set the url as Moshtix,
url = "http://www.moshtix.com.au/v2/event/splendour-in-the-grass-2018/103360"
# set the headers like we are a browser,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
}

while True:
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")


    # if the number of times the word "Google" occurs on the page is less than 1,
    if soup.find(class_="col-quantity col-quantity-216701").find('select') is None:
        # wait 60 seconds,
        print("Refresh #" + str(count))
        count+=1
        time.sleep(1)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        #pyautogui.click( )
        winsound.PlaySound('pop.mp3', winsound.SND_FILENAME)
        print(time.asctime())
        with open("log.txt", "a") as myfile:
            myfile.write(time.asctime())
        webbrowser.open(url)
