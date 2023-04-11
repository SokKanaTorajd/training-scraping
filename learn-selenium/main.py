from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import pandas as pd

options = Options()

# # option for display the browser
# options.add_experimental_option("detach", True)

# options for making the browser headless
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

driver = Chrome(executable_path='/d/Sadasa Academy/training-scraping/learn-selenium/chromedriver.exe', options=options)

# scrape sarung in bhinneka.com
keyword = 'sarung'
base_url = 'https://www.bhinneka.com/jual?cari='
url = base_url+keyword
page_param = '&page='

driver.get(url)
driver.implicitly_wait(10)


# close pop up function
def close_popup(driver):
    popup_button = driver.find_element(by=By.XPATH, value='//*[@id="onesignal-slidedown-cancel-button"]')
    popup_button.click()

try:
    close_popup(driver)

except ElementClickInterceptedException:
    close_popup(driver)

except NoSuchElementException:
    pass

# get maximum page
max_page_xpath = '//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div[41]/div/button[5]'
max_result_page = driver.find_element(by=By.XPATH, value=max_page_xpath).text
max_result_page = int(max_result_page)

data = []

for i in range(2, max_result_page+1):
    driver.implicitly_wait(10)

    results = driver.find_elements(by=By.XPATH, value='//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div')
    for result in results:
        try:
            index = results.index(result)+1
            xpath_url = f'//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div[{index}]/div/a'
            product_url = result.find_element(by=By.XPATH, value=xpath_url).get_attribute('href')

        except NoSuchElementException:
            product_url = None
        
        data.append(product_url)
    
    url = url+page_param+str(i)
    driver.get(url)
    driver.implicitly_wait(10)

    # revert url back to its original state
    url = base_url+keyword

# convert list to dataframe
df = pd.DataFrame(data, columns=['url'])

# save to csv file
df.to_csv(f'scrape-bhinneka-sarung-url.csv', index=False)

driver.close()
