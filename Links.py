from selenium import webdriver
from selenium.webdriver.common import keys
import  time
import  stopwatch

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('http://www.newtours.demoaut.com')
driver.maximize_window()
links = driver.find_elements_by_tag_name('a')
print('Number of links : ',len(links))
for link in links:
    print(link.text)

driver.find_element_by_partial_link_text('REG').click()
time.sleep(10)
driver.close()