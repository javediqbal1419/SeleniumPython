from  selenium import webdriver
import time

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    driver.get('http://mmaplus.rtdtradetracker.com')
    driver.find_element_by_name('userName').send_keys('developer')
    driver.find_element_by_name('password').send_keys('developer@1122')
    driver.find_element_by_name('Submit').click()

def test_teardown():
    time.sleep(5)
    driver.close()
