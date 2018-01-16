# -*- coding: utf-8 -*-
from selenium import webdriver
from model.data import Data
from random import choice
from string import digits
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class Appliaction:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def open_station(self):
        driver = self.driver
        driver.get("https://172.20.9.134/#!/login")

    def user_login(self, userName, admPass):
        driver = self.driver
        self.open_station()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(userName)
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(admPass)
        driver.find_element_by_xpath("//input[@value='Log In']").click()

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
        self.logout()

    def logout(self):
        driver = self.driver
        logoutBtn = driver.find_element_by_xpath("(//a[contains(@href, '#')])[20]")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()

    def destroy(self):
        self.driver.quit()
