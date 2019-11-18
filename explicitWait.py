from selenium import webdriver
from selenium.webdriver.common import keys
import  time

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('http://mmaplus.rtdtradetracker.com/')
driver.maximize_window()
driver.close()