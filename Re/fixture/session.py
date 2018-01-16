# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_as_admin(self, userName, admPass):
        driver = self.app.driver
        self.app.open_station()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(userName)
        driver.find_element_by_xpath("//input[@type='password']").send_keys(admPass)
        driver.find_element_by_xpath("//input[@value='Log In']").click()

    def logout(self):
        driver = self.app.driver
        logoutBtn = driver.find_element_by_xpath("(//a[contains(@href, '#')])[20]")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()
