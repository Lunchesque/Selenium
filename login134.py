# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest, time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_login_all_users(self):

        driver = self.driver
        driver.get("https://172.20.9.134")

        driver.find_element_by_xpath("//input[@type='text']").send_keys("999")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admADM1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[20]").click()
        driver.find_element_by_link_text(u"Выйти").click()

        time.sleep(0.1)
        #driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("888")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("operOPER1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()
        driver.find_element_by_css_selector("div.toolbar-icon-container-item.ng-scope > svg.kp-u-icon").click()
        driver.find_element_by_link_text(u"Выйти").click()

        time.sleep(0.1)
        #driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("777")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("nabNAB1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()
        driver.find_element_by_css_selector("div.toolbar-icon-container-item.ng-scope > svg.kp-u-icon").click()
        driver.find_element_by_link_text(u"Выйти").click()

        time.sleep(0.1)
        #driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("666")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("gueGUE1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()
        driver.find_element_by_css_selector("div.toolbar-icon-container-item.ng-scope > svg.kp-u-icon").click()
        driver.find_element_by_link_text(u"Выйти").click()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
