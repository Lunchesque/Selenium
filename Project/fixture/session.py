# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_station(self):
        driver = self.app.driver
        driver.get("https://172.20.9.134/#!/login")


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
        logoutBtn = driver.find_element_by_css_selector("img.img-circle.toolbar-icon-container-item.ng-scope")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()

    def ensure_logout(self):
        driver = self.app.driver
        if len(driver.find_elements_by_css_selector("img.img-circle.toolbar-icon-container-item.ng-scope")) > 0:
            self.logout()

    def being_on_users_page(self):
        driver = self.app.driver
        if  not driver.current_url == "https://172.20.9.134/#!/org/users":
            self.open_users_list()
        else:
            pass
