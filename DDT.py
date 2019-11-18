import  openpyxl
import DDTbase
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
driver.get('http://mmaplus.rtdtradetracker.com')
driver.maximize_window()
path="C:/Users/javed iqbal/Box Sync/selenium/userPassword.xlsx"
rows = DDTbase.getRowCount(path,'Sheet1')
print(rows)
for r in range(2, rows+1):
    userName=DDTbase.readData(path, "Sheet1", r, 1)
    password=DDTbase.readData(path, "Sheet1", r, 2)
    driver.find_element_by_name('userName').send_keys(userName)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('Submit').click()

    if driver.find_element_by_id('logo'):
        print('Test case is Pass')
        DDTbase.writeData(path, "Sheet1", r, 3, 'Test Passed')
    else:
        print('Test is failed')
        DDTbase.writeData(path, "Sheet1", r, 3, 'Test Failed')
    driver.get('http://mmaplus.rtdtradetracker.com')