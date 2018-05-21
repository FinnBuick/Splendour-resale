# Import requests (to download the page)
import requests
import winsound

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# set the url as Moshtix,
url = "http://www.moshtix.com.au/v2/event/splendour-in-the-grass-2018/103360"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\finnb\\AppData\\Local\\Google\\Chrome\\User Data")
#options.add_argument('--load-extension=C:\\Users\\finnb\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\noaebbfkkfkacibllmggddgcmccflooj\\1.0.0.1_0')
#options.add_argument("--headless")
options.add_argument('--no-proxy-server')
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\ChromeDriver\\chromedriver.exe" , chrome_options=options)
driver.get(url)

def check_exists_by_css_selector(selector):
    try:
        driver.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return False
    return True

count = 0
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
    # if soup.find(class_="col-quantity col-quantity-216690").find('select') is None:
    #     # wait 60 seconds,
    #     print("Trying again...")
    #     #time.sleep(1)
    #     # continue with the script,
    #     continue

    if soup.find(class_="col-quantity col-quantity-216690").find('select') is None:
        print("Refresh #" + str(count))
        count+=1
        time.sleep(1)

        continue

    # but if the word "Google" occurs any other number of times,
    else:
        winsound.PlaySound('pop.mp3', winsound.SND_FILENAME)
        driver.get(url)
        select = Select(driver.find_element_by_name('lQuantity0'))
        select.select_by_index(1)

        print("Selecting no. of tickets...")

        driver.find_element_by_id('event-buy-tickets').click()

        print("Buy clicked")

        #next page

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "purchase-add-ons")))
        cont = driver.find_element_by_id('purchase-add-ons')
        cont.click()

        print("Clicking continue...")

        #next page

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'payment-details-header')))

        time.sleep(1)

        el = driver.find_element_by_name('dob-day')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '23':
                option.click()  # select() in earlier versions of webdriver
                break

        el = driver.find_element_by_name('dob-month')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'AUG':
                option.click()  # select() in earlier versions of webdriver
                break

        el = driver.find_element_by_name('dob-year')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '1996':
                option.click()  # select() in earlier versions of webdriver
                break

        print("DOB entered...")

        tcs = driver.find_element_by_id('accept-terms-conditions')
        tcs.click()

        print("T&Cs clicked...")

        payMethod = driver.find_element_by_id('clientPaymentMethod_option_creditcard_mc')
        payMethod.click()

        print("Payment method clicked...")

        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pay-now')))

        time.sleep(5)

        cardName = driver.find_element_by_id('payment_request_card_holder')
        cardName.send_keys('Finneas Buick')

        cardNo = driver.find_element_by_id('payment_request_card_number')
        cardNo.send_keys('5280133656090049')

        expMonth = Select(driver.find_element_by_id('payment_request_expiry_month'))
        expMonth.select_by_value('7')

        expYear = Select(driver.find_element_by_id('payment_request_expiry_year'))
        expYear.select_by_value('2018')

        code = driver.find_element_by_id('payment_request_security_code')
        code.send_keys('998')

        pay = driver.find_element_by_id('pay-now')
        pay.click()

        break