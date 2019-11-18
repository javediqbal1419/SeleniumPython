from selenium import webdriver
from selenium.webdriver.common import keys
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):      # it run only once
        cls.driver = driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_marksman(self):
        self.driver.get('https://www.google.com.pk')
        self.driver.find_element_by_name('q').send_keys('marksman.com.pk')
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(keys.Keys.ENTER)

    def test_search_javed(self):
        self.driver.get('https://www.google.com.pk')
        self.driver.find_element_by_name('q').send_keys('javediqbal1419.github.io')
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(keys.Keys.ENTER)

    @classmethod
    def tearDown(cls):  # it will once after the test
        cls.driver.close()
        cls.driver.quit()
        print('Test Pass')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/javed iqbal/Box Sync/selenium/StepByStep/unitTestReports'))


