from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class MMAPlusTest02(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_m_m_a_plus_test02(self):
        driver = self.driver
        driver.get("http://mmaplus.rtdtradetracker.com/")
        driver.maximize_window()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("developer")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("developer@1122")
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Out of Stock Summary'])[2]/following::span[1]").click()
        driver.find_element_by_link_text("Merchandiser Daily Visit - PDF").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        time.sleep(10)
        driver.find_element_by_id("zoneId").click()
        # driver.find_element_by_id('zoneId').click()

        Select(driver.find_element_by_id('zoneId')).select_by_visible_text('Center')
        driver.find_element_by_id('zoneId').click()
        driver.find_element_by_id("regionId").click()
        Select(driver.find_element_by_id('regionId')).select_by_visible_text("Lahore A")
        driver.find_element_by_id("regionId").click()
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_link_text("14").click()
        driver.find_element_by_id("surveyorId").click()
        Select(driver.find_element_by_id("surveyorId")).select_by_visible_text("LHR-A001 - Hassan Yousaf")
        driver.find_element_by_id("surveyorId").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Auditor:'])[1]/following::i[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    @classmethod
    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
