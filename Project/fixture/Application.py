# -*- coding: utf-8 -*-

from random import choice
from string import digits
from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.driver.maximize_window()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

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
        a = 1
        autoNum = driver.find_elements_by_xpath("(//tr/td/span[contains(@title, 'Auto.test.user')])")
        count = len(autoNum)
        if count == 0:
            pass
        elif count != 0:
            while count != 0:
                title = driver.find_element_by_xpath("(//span[contains(@ng-bind, 'full_name')])[{}]".format(a)).get_attribute("title")
                if "Auto.test.user" in title:
                    btnNum = 5 + a
                    ActionChains(driver).pause(0.05).perform()
                    optionsBtn = driver.find_element_by_xpath("(//button[@type='button'])[{}]".format(btnNum))
                    ActionChains(driver).move_to_element(optionsBtn).click(optionsBtn).perform()
                    driver.find_element_by_link_text(u"Удалить").click()
                    driver.find_element_by_xpath("//div[3]/button[contains(@class, 'primary')]").click()
                    count -= 1
                else:
                    a += 1

    def destruction(self):
        self.driver.quit()
