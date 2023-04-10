from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

options = Options()
options.add_experimental_option("detach", True)
driver = Chrome(executable_path='/d/Sadasa Academy/training-scraping/learn-selenium/chromedriver.exe', options=options)

# load url
driver.get('https://www.youtube.com/watch?v=6-aVQl69DAg')
driver.implicitly_wait(10)

# scroll youtube video page to load youtube comments
driver.execute_script("window.scrollTo(0, 1080)")
