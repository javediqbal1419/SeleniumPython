from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('http://mmaplus.rtdtradetracker.com')
driver.maximize_window()
cooki=driver.get_cookie()
print(cooki)
driver.find_element_by_name('userName').send_keys('developer')
driver.find_element_by_name('password').send_keys('developer@1122')
driver.find_element_by_name('Submit').click()
print(driver.title)