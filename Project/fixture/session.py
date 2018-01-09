# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_station(self):
        driver = self.app.driver
        driver.get("http://172.20.9.134")

    def login_as_admin(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@type='text']").send_keys("999")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admADM1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()

    def logout(self):
        driver = self.app.driver
        logoutBtn = driver.find_element_by_xpath("(//a[contains(@href, '#')])[20]")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()
