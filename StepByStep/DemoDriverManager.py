from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver
# from webdriver_manager


driver = webdriver.Ie(IEDriverManager().install())
driver.get("http://www.google.com/")
print (driver.title)
driver.quit()