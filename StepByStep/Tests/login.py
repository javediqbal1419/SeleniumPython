from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from StepByStep.Pages.LoginPage import LoginPage
from StepByStep.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()l

    def test_login_valid(self):
        driver = self.driver
        driver.get('http://mmaplus.rtdtradetracker.com')
        login = LoginPage(driver)
        login.enter_username('developer')
        login.enter_password('developer@1122')
        login.click_login()

    def test_logout(self):
        driver = self.driver

        homePage = HomePage(driver)
        homePage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Test Completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/javed iqbal/Box Sync/selenium/StepByStep'))



