from selenium import webdriver
from selenium.webdriver.common import keys
import  time
import  stopwatch

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()
# 1. Scroll by pixel
# driver.execute_script("window.scrollTo(0, 1000);")

# 2. Scroll Page to find element
flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[35]/td[1]/img')
driver.execute_script("arguments[0].scrollIntoView();",flag)

# 3. Scroll till end
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# driver.close()