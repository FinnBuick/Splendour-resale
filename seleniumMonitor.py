# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# set the url as Moshtix,
url = "http://www.moshtix.com.au/v2/event/splendour-in-the-grass-2018/103360"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\finnb\\AppData\\Local\\Google\\Chrome\\User Data")
#options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\ChromeDriver\\chromedriver.exe" , chrome_options=options)
driver.get(url)


# while this is true (it is true by default),
while True:

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
        print("Trying again...")
        #time.sleep(1)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        driver.get(url)
        select = Select(driver.find_element_by_css_selector('#event-tickets-form > table > tbody > tr:nth-child(2) > td.col-quantity.col-quantity-216690 > select'))
        select.select_by_index(1)
        driver.find_element_by_css_selector('#event-buy-tickets').click()
        #next page

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "attendee-individual-names-table")))

        day = driver.find_element_by_css_selector('#attendee-individual-names-table > table:nth-child(2) > tbody > tr.attendee-row > td.attendee-dob.dob-column > div > select:nth-child(1)')
        day.select_by_value('23')
        month = driver.find_element_by_css_selector('#attendee-individual-names-table > table:nth-child(2) > tbody > tr.attendee-row > td.attendee-dob.dob-column > div > select:nth-child(2)')
        month.select_by_value('AUG')
        year = driver.find_element_by_css_selector('#attendee-individual-names-table > table:nth-child(2) > tbody > tr.attendee-row > td.attendee-dob.dob-column > div > select:nth-child(3)')
        year.select_by_value('1996')

        tcs = driver.find_element_by_css_selector('#accept-terms-conditions')
        tcs.click()

        break