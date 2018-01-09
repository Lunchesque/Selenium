# -*- coding: utf-8 -*-

from random import choice
from string import digits
from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.driver.maximize_window()

    def create_all_types_of_users(self, index):
        driver = self.driver
        addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")
        ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()
        select = Select(driver.find_element_by_name("role")).select_by_index(index)

        role = driver.find_element_by_name("role").get_attribute("value")
        userId = (''.join(choice(digits) for i in range(5)))
        email = ("AutoTestUser_{0}_{1}@ki.ki".format(role, userId))
        phone = (''.join(choice(digits) for i in range(15)))
        fullName = ("Auto.test.user_{0}_{1}".format(role, userId))
        password = fullName

        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("phone").send_keys(phone)
        driver.find_element_by_name("fullName").send_keys(fullName)

        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()

        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("password_confirmation").send_keys(password)

        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

    def deletion_auto_users(self):
        driver = self.driver
        optionsBtn = driver.find_element_by_xpath("(//button[@type='button'])[6]")
        ActionChains(driver).move_to_element(optionsBtn).click(optionsBtn).perform()
        driver.find_element_by_link_text(u"Удалить").click()
        driver.find_element_by_xpath("//div[3]/button[contains(@class, 'primary')]").click()

    def deletion_circle(self):
        deletion = True
        driver = self.driver
        title = driver.find_element_by_xpath("(//tr/td/span[contains(@ng-bind, 'user')])[1]").get_attribute("title")
        while deletion:
            if "Auto.test.user_" in title:
                self.deletion_auto_users()
                ActionChains(driver).pause(0.05).perform()
            else:
                print("No AutoTestUsers Found")
                deletion = False
            title = driver.find_element_by_xpath("(//tr/td/span[contains(@ng-bind, 'user')])[1]").get_attribute("title")


    def destruction(self):
        self.driver.close()
