from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')

driver.maximize_window()
driver.get('https://www.google.com.pk')
name=driver.find_element_by_name('q').send_keys('marksman.com.pk')

driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(keys.Keys.ENTER)
