from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

options = Options()
options.add_experimental_option("detach", True)
driver = Chrome(executable_path='/d/Sadasa Academy/training-scraping/learn-selenium/chromedriver.exe', options=options)

# driver.get('https://facebook.com')
# driver.implicitly_wait(10)

# # get email element
# email_box = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
# email_box.send_keys("wijatama@gmail.com")

# # get password element
# password_box = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
# password_box.send_keys("password123")

# # click button login
# login_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
# login_button.click()

# scrape youtube comments

# driver.get('https://www.youtube.com/watch?v=6-aVQl69DAg')
# driver.implicitly_wait(10)

# driver.execute_script("window.scrollTo(0, 1080)")

driver.get('https://www.bhinneka.com/')
driver.implicitly_wait(10)

# close pop up
def close_popup(driver):
    popup_button = driver.find_element(by=By.XPATH, value='//*[@id="onesignal-slidedown-cancel-button"]')
    popup_button.click()

try:
    close_popup(driver)
except ElementClickInterceptedException:
    close_popup(driver)

# search bar
search_bar = driver.find_element(by=By.XPATH, value='//*[@id="searchProduct"]')
search_bar.click()
driver.implicitly_wait(5)
search = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/div/div/header/div/div[2]/div/div/input')
search.send_keys("sarung")

search_button = driver.find_element(by=By.XPATH, value='//*[@id="searchProduct"]/div/div/div/button')
search_button.click()
# search_button.click()

driver.implicitly_wait(10)

# max_page = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div[41]/div/button[5]').text
# max_page = int(max_page)


data = []
for i in range(3):
    results = driver.find_elements(by=By.XPATH, value='//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div')
    print(len(results))
    for result in results:
        try:
            index = results.index(result)+1
            # image_url = result.find_element(by=By.XPATH, value=f'//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div[{index}]/div/a/img').get_attribute('href')
            product_title = result.find_element(By.XPATH, value=f'//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div[{index}]/div/a/div[2]/div[1]/p').text
            price = result.find_element(by=By.XPATH, value=f'//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div[{index}]/div/a/div[2]/div[2]/div[2]').text
            print(product_title)
            data.append([product_title, price])

        except NoSuchElementException:
            pass

    # next button
    next = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[4]/div[2]/div[2]/div[3]/div[2]/div[41]/div/button[6]')
    driver.implicitly_wait(7)

print(data)
