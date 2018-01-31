# -*- coding: utf-8 -*-
from fixture import application
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_as_admin(self, userName, admPass):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@type='text']").send_keys(userName)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(admPass)
        driver.find_element_by_xpath("//input[@value='Log In']").click()

    def open_users_list(self):
        driver = self.app.driver
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_link_text(u"Пользователи").click()

    def logout(self):
        driver = self.app.driver
        logoutBtn = driver.find_element_by_xpath("(//a[@href='#'])[5]")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()

    def ensure_logout(self):
        driver = self.app.driver
        if len(driver.find_elements_by_xpath("(//a[@href='#'])[5]")) > 0:
            self.logout()

    def being_on_users_page(self):
        driver = self.app.driver
        if  not driver.current_url == "https://172.20.9.134/#!/org/users":
            self.open_users_list()
        else:
            pass

    def login_gmail(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@type='email']").send_keys("sergey.verkhovodko@synesis.ru")
        driver.find_element_by_xpath("//content/span").click()
        driver.find_element_by_name("password").send_keys("19051993abcd")
        ActionChains(driver).pause(0.2).perform()
        driver.find_element_by_xpath("//div[2]/div/div/content").click()
