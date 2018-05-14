# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

from selenium import webdriver

# set the url as VentureBeat,
url = "http://www.moshtix.com.au/v2/event/splendour-in-the-grass-2018/103360"
# set the headers like we are a browser,
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# download the homepage
response = requests.get(url, headers=headers)
# parse the downloaded homepage and grab all text, then,
soup = BeautifulSoup(response.text, "lxml")



if __name__ == "__main__":
    webbrowser.open(url)
    print(soup.find(class_="col-quantity col-quantity-216690").find('select'))

    # event-tickets-form > table > tbody > tr:nth-child(4) > td.col-quantity.col-quantity-216691 > select