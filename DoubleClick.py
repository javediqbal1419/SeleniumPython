from selenium import webdriver
from selenium.webdriver.common import keys
import  time
from selenium.webdriver import  ActionChains

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('https://testautomationpractice.blogpost.com')
driver.maximize_window()
element=driver.find_element_by_xpath('')
actions=ActionChains(driver)
actions.double_click(element).perform()