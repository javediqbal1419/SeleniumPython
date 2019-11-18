# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class MMAPlusTest01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_m_m_a_plus_test01(self):
        driver = self.driver
        driver.get("http://mmaplus.rtdtradetracker.com/")
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
        driver.find_element_by_id("zoneId").click()
        Select(driver.find_element_by_id("zoneId")).select_by_visible_text("Center")
        driver.find_element_by_id("zoneId").click()
        driver.find_element_by_id("regionId").click()
        Select(driver.find_element_by_id("regionId")).select_by_visible_text("Lahore A")
        driver.find_element_by_id("regionId").click()
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_link_text("15").click()
        driver.find_element_by_id("surveyorId").click()
        Select(driver.find_element_by_id("surveyorId")).select_by_visible_text("LHR-A001 - Hassan Yousaf")
        driver.find_element_by_id("surveyorId").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Auditor:'])[1]/following::i[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_link_text("Merchandiser Productivity Report").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("zoneId").click()
        Select(driver.find_element_by_id("zoneId")).select_by_visible_text("Center")
        driver.find_element_by_id("zoneId").click()
        driver.find_element_by_id("regionId").click()
        Select(driver.find_element_by_id("regionId")).select_by_visible_text("Lahore A")
        driver.find_element_by_id("regionId").click()
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_link_text("15").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Remove Impact:'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='None selected'])[1]/following::label[1]").click()
        driver.find_element_by_xpath("//form[@id='merchActivityReportForm']/table").click()
        driver.find_element_by_id("btnId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Out of Stock Summary'])[2]/following::span[1]").click()
        driver.find_element_by_link_text("Score Card").click()
        driver.find_element_by_link_text("Shop List by Score").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("projectType").click()
        Select(driver.find_element_by_id("projectType")).select_by_visible_text("Mma Plus")
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
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_id("endDate").click()
        driver.find_element_by_link_text("15").click()
        driver.find_element_by_id("shopsType").click()
        driver.find_element_by_id("shopsType").click()
        driver.find_element_by_id("channelTypeId").click()
        driver.find_element_by_id("channelTypeId").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Channels:'])[1]/following::button[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Channels:'])[1]/following::label[1]").click()
        driver.find_element_by_id("scoreLimit").click()
        driver.find_element_by_id("scoreLimit").click()
        driver.find_element_by_id("scoreTypeReport").click()
        driver.find_element_by_id("scoreTypeReport").click()
        driver.find_element_by_id("scoreType").click()
        Select(driver.find_element_by_id("scoreType")).select_by_visible_text("MMA_Plus Scoring Report")
        driver.find_element_by_id("scoreType").click()
        driver.find_element_by_id("visitsType").click()
        driver.find_element_by_id("visitsType").click()
        driver.find_element_by_id("criteria").click()
        driver.find_element_by_id("criteria").click()
        driver.find_element_by_id("btnId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Complaint Tracking Summary'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Hanger Shops List").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("actionType").click()
        driver.find_element_by_id("actionType").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_link_text("15").click()
        driver.find_element_by_id("btnId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
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
        driver.find_element_by_id("zoneId").click()
        Select(driver.find_element_by_id("zoneId")).select_by_visible_text("Center")
        driver.find_element_by_id("zoneId").click()
        driver.find_element_by_id("regionId").click()
        Select(driver.find_element_by_id("regionId")).select_by_visible_text("Lahore A")
        driver.find_element_by_id("regionId").click()
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_link_text("13").click()
        driver.find_element_by_id("surveyorId").click()
        driver.find_element_by_id("surveyorId").click()
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

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
