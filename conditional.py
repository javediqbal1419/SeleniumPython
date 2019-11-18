from selenium import webdriver
from selenium.webdriver.common import keys
import  time

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('http://mmaplus.rtdtradetracker.com/')
driver.maximize_window()
driver.find_element_by_name('userName').send_keys("Developer")
driver.find_element_by_name('password').send_keys("Developer@1122")
driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[3]/div/button').click()
time.sleep(10)
driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[1]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[1]/ul/li[1]/a').click()
