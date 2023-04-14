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
# options.add_experimental_option("detach", True)

# options for making the browser headless
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

driver = Chrome(executable_path='/d/Sadasa Academy/training-scraping/learn-selenium/chromedriver.exe', 
                options=options)

def close_popup(driver):
    popup_button = driver.find_element(by=By.XPATH, value='//*[@id="onesignal-slidedown-cancel-button"]')
    popup_button.click()


product_details = []

for i in range(len(urls)):
    try:
        driver.get(urls[i])
        driver.implicitly_wait(7)

    except NoSuchElementException:
        close_popup()
        driver.get(urls[i])
        driver.implicitly_wait(7)

    try:
        # get product title
        title_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/h1'
        product_title = driver.find_element(by=By.XPATH, value=title_xpath).text

    except NoSuchElementException:
        product_title = 'Unsuccessful'

    try:
        # get product price
        price_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/div[3]/div/div/h4'
        product_price = driver.find_element(by=By.XPATH, value=price_xpath).text

    except NoSuchElementException:
        product_price = 'Unsuccessful'

    try:
        # get product code
        product_code_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/div[2]/div[1]/span'
        product_code = driver.find_element(by=By.XPATH, value=product_code_xpath).text

    except NoSuchElementException:
        product_code = 'Unsuccessful'

    try:
        # get shop's name
        try:
            shop_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/div[7]/div/a'
            shop_name = driver.find_element(by=By.XPATH, value=shop_xpath).text
        
        except NoSuchElementException:
            shop_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[2]/div/div[8]/div/a'
            shop_name = driver.find_element(by=By.XPATH, value=shop_xpath).text
    
    except NoSuchElementException:
        shop_name = 'Unsuccessful'

    detail = {
        'product_title' : product_title,
        'product_price' : product_price,
        'product_code'  : product_code,
        'shop_name'     : shop_name
    }

    product_details.append(detail)
    print(f'scraped ke-{i+1}')


# convert list to dataframe
df = pd.DataFrame(product_details)

# save to csv file
df.to_csv('hasil-scrape-bhinneka-detail-produk-sarung-url.csv', index=False)

# close driver
print('scraping selesai.')
driver.close()
