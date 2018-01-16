# -*- coding: utf-8 -*-
from random import choice
from string import digits
from model.data import Data
from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Appliaction:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)

    def open_station(self):
        driver = self.driver
        driver.get("https://172.20.9.134/#!/login")

    def open_users_list(self):
        driver = self.driver
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_link_text(u"Пользователи").click()

    def creating_admin(self, data):
        driver = self.driver
        self.open_users_list()
        driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]").click()
        driver.find_element_by_name("email").send_keys(data.email.format(data.userId))
        driver.find_element_by_name("phone").send_keys(data.phone)
        driver.find_element_by_name("fullName").send_keys(data.name.format(data.userId))
        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()
        driver.find_element_by_name("password").send_keys(data.name.format(data.userId))
        driver.find_element_by_name("password_confirmation").send_keys(data.name.format(data.userId))
        Select(driver.find_element_by_name("role")).select_by_visible_text(u"Администратор")
        driver.find_element_by_name("role").click()
        driver.find_element_by_name("enableNotifications").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        ActionChains(driver).pause(0.05).perform()
        self.session.logout()

    def destroy(self):
        self.driver.quit()
