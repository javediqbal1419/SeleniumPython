# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class MMAPlusTest04(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\SelTest\driver\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_m_m_a_plus_test04(self):
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
            "(.//*[normalize-space(text()) and normalize-space(.)='View Pops'])[1]/following::span[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="112"]/a').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        # driver.find_element_by_id("isNpl").click()
        # driver.find_element_by_id("isNpl").click()
        Select(driver.find_element_by_xpath('//*[@id="projectType"]')).select_by_visible_text('Nestle')
        # driver.find_element_by_id("projectType").click()
        Select(driver.find_element_by_xpath('//*[@id="projectType"]')).select_by_visible_text("Mma Plus")
        driver.find_element_by_id("projectType").click()
        driver.find_element_by_id("actionType").click()
        Select(driver.find_element_by_id("actionType")).select_by_visible_text("Regional")
        driver.find_element_by_id("actionType").click()
        driver.find_element_by_id("zoneId").click()
        Select(driver.find_element_by_id("zoneId")).select_by_visible_text("Center")
        driver.find_element_by_id("zoneId").click()
        driver.find_element_by_id("regionId").click()
        Select(driver.find_element_by_id("regionId")).select_by_visible_text("Lahore A")
        driver.find_element_by_id("regionId").click()
        driver.find_element_by_id("category").click()
        Select(driver.find_element_by_id("category")).select_by_visible_text("Chiller")
        driver.find_element_by_id("category").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Product List'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='None selected'])[4]/following::label[1]").click()
        driver.find_element_by_id("mustHave").click()
        driver.find_element_by_id("mustHave").click()
        driver.find_element_by_id("yogurtAllocation").click()
        Select(driver.find_element_by_id("yogurtAllocation")).select_by_visible_text("Yes")
        driver.find_element_by_id("yogurtAllocation").click()
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_link_text("14").click()
        driver.find_element_by_id("endDate").click()
        driver.find_element_by_link_text("18").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Channels:'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Channels:'])[1]/following::label[1]").click()
        driver.find_element_by_id("chillerAllocated").click()
        driver.find_element_by_id("chillerAllocated").click()
        driver.find_element_by_id("btnId").click()

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

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
