from selenium import webdriver
from selenium.webdriver.common import keys
import  time
# import unittest
# import HtmlTestRunner

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('https://www.google.com.pk')
driver.find_element_by_name('q').send_keys('Javed')
time.sleep(10)
print(driver.title)
print(driver.current_url)
driver.close()