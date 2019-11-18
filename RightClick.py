from selenium import webdriver
from selenium.webdriver.common import keys
import  time
from selenium.webdriver import  ActionChains

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('https://javediqbal1419.github.io')
driver.maximize_window()
button=driver.find_element_by_xpath('//*[@id="profile"]/div/h3[2]/a/span')
print(button.text)
actions=ActionChains(driver)
actions.context_click(button).perform()