from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import pandas as pd


# load data url
df = pd.read_csv('D:/Sadasa Academy/training-scraping/learn-selenium/scrape-bhinneka-sarung-url.csv')
df = df.dropna()
urls = df['url'].values.tolist()

options = Options()
options.add_experimental_option("detach", True)

driver = Chrome(executable_path='/d/Sadasa Academy/training-scraping/learn-selenium/chromedriver.exe', 
                options=options)

def close_popup(driver):
    popup_button = driver.find_element(by=By.XPATH, value='//*[@id="onesignal-slidedown-cancel-button"]')
    popup_button.click()


product_details = []

for i in range(5):
    try:
        driver.get(urls[i])
        driver.implicitly_wait(10)

    except NoSuchElementException:
        close_popup()
        driver.get(urls[i])
        driver.implicitly_wait(10)

    # get product title
    title_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/h1'
    product_title = driver.find_element(by=By.XPATH, value=title_xpath).text

    # get product price
    price_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/div[3]/div/div/h4'
    product_price = driver.find_element(by=By.XPATH, value=price_xpath).text

    # get product code
    product_code_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/div[2]/div[1]/span'
    product_code = driver.find_element(by=By.XPATH, value=product_code_xpath).text

    # get shop's name
    shop_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/div[7]/div/a'
    shop_name = driver.find_element(by=By.XPATH, value=shop_xpath).text

    detail = {
        'product_title' : product_title,
        'product_price' : product_price,
        'product_code'  : product_code,
        'shop_name'     : shop_name
    }

    product_details.append(detail)
    print(detail)

# close driver
driver.close()
