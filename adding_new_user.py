# -*- coding: utf-8 -*-
import unittest, time, re
from random import choice
from string import digits
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def open_station(self, driver):
        driver.get("https://172.20.9.134/#!/login")

    def user_login(self, driver, userName, admPass):
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(userName)
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(admPass)
        driver.find_element_by_xpath("//input[@value='Log In']").click()

    def open_users_list(self, driver):
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_link_text(u"Пользователи").click()

    def creating_admin(self, driver, email, name):
        userId = (''.join(choice(digits) for i in range(5)))    #генерация уникального рандомного идентификатора пользователя
        driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email.format(userId))
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys(''.join(choice(digits) for i in range(15)))
        driver.find_element_by_name("fullName").clear()
        driver.find_element_by_name("fullName").send_keys(name.format(userId))
        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(name.format(userId))
        driver.find_element_by_name("password_confirmation").send_keys(name.format(userId))
        Select(driver.find_element_by_name("role")).select_by_visible_text(u"Администратор")
        driver.find_element_by_name("role").click()
        driver.find_element_by_name("enableNotifications").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

    def logout(self, driver):
        logoutBtn = driver.find_element_by_xpath("(//a[contains(@href, '#')])[20]")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()

    def test_untitled_test_case(self):
        driver = self.driver
        self.open_station(driver)
        self.user_login(driver, userName = "999", admPass = "admADM1/")
        self.open_users_list(driver)
        self.creating_admin(driver, email = "AutoTestUser_{0}@ki.ki", name = "Auto.test.user_{0}")
        ActionChains(driver).pause(0.05).perform()
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
