#importing libraries
import time
import getpass
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#print("Enter facebook email id: ")
#email = str(input())
#password = getpass.getpass("Enter facebook password: ")
email='7557078998'
password='LocalHost128'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver')
#chrome_options = Options()
#options.addArguments("--incognito")
#DesiredCapabilities capabilities = DesiredCapabilities.chrome()
#capabilities.setCapability(ChromeOptions.CAPABILITY, options)

driver.get('https://www.facebook.com/') 

search = driver.find_elements_by_id('email')[0].clear()
search = driver.find_elements_by_id('email')[0]
search.send_keys(email)
search = driver.find_elements_by_id('pass')[0].clear()
search = driver.find_elements_by_id('pass')[0]
search.send_keys(password)
search.send_keys(Keys.RETURN)


time.sleep(4)
a = driver.find_elements_by_xpath("//input[@placeholder='Search']")[0]
a.send_keys("Business Club, IIT Kharagpur")
a.send_keys(Keys.RETURN)


time.sleep(4)
timeline = driver.find_elements_by_xpath("//a[contains(text(), 'Business Club, IIT Kharagpur')]")[0]
timeline.click()

# +
#time.sleep(7)
#SCROLL_PAUSE_TIME = 0.5
# -

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# i = 0
# while i<1:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#     i+=1

# u_8e_0 > div > ul > li._54ni._2al8.__MenuItem > a > span > span

share_button = driver.find_element_by_xpath("//a[contains(text(), 'Share')]")

share_button.click()
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
share = WebDriverWait(driver, 2,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, '//li[@class="_54ni _2al8 __MenuItem"]/a[@role="menuitem"]')))
share.click()

time.sleep(2)

include_original = WebDriverWait(driver, 2,ignored_exceptions=ignored_exceptions)\
                         .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[@class="_66ul"]')))
include_original.click()

post = WebDriverWait(driver, 2,ignored_exceptions=ignored_exceptions)\
                         .until(expected_conditions.presence_of_element_located((By.XPATH, '//button[@class="_2g61 _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]')))
post.click()
print("Posted Successfully!")


