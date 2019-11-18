from  selenium import webdriver
# from  webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Ie(IEDriverManager().install())
driver.get('http://mmaplus.rtdtradetracker.com')
driver.maximize_window()
driver.find_element_by_name('userName').send_keys('developer')
driver.find_element_by_name('password').send_keys('developer@1122')
driver.find_element_by_name('Submit').click()
driver.close()
print(driver.title)