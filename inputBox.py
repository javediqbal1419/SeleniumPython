from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
import  time

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('http://localhost:8081/vuproject/login.jsp')
driver.maximize_window()
driver.find_element_by_name('name').send_keys('qa')
driver.find_element_by_name('password').send_keys('12')
# driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/form/div[4]/div[1]/button').click()

driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/a').click()
total_fields = driver.find_elements_by_class_name('form-control')
print(len(total_fields))
status = driver.find_element_by_name('user').is_enabled()
print(status)
driver.find_element_by_name('user').send_keys('javed123')
driver.find_element_by_name('firstName').send_keys('Javed')
driver.find_element_by_name('lastName').send_keys('Khan')
driver.find_element_by_name('email').send_keys('company@marksman.com.pk')
driver.find_element_by_name('pass1').send_keys('123')
driver.find_element_by_name('pass').send_keys('123')
drop = driver.find_element_by_name('userRole')
drp = Select(drop)
# print(len(drp.options))
allOption = drp.options
for options in allOption:
    print(options.text)
drp.select_by_value('5')
# driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/form/div[8]/button[1]').click()