from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

options = Options()
options.add_experimental_option("detach", True)
driver = Chrome(executable_path='/d/Sadasa Academy/training-scraping/learn-selenium/chromedriver.exe', options=options)

# load url
driver.get('https://facebook.com')
driver.implicitly_wait(10)

# get email element
email_box = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
email_box.send_keys("wijatama@gmail.com")

# get password element
password_box = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
password_box.send_keys("password123")

# click button login
login_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
login_button.click()
