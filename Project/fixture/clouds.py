# -*- coding: utf-8 -*-
import os
from model.data import Data
from fixture import application
from fixture.session import SessionHelper
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class CloudsHelper:

    def __init__(self, app):
        self.app = app

    def add_cloud(self):
        driver = self.app.driver
        self.app.session.open_org_view()
        driver.find_element_by_xpath("//button[@id='copy_vpnlink']").click()
        vpnlink = os.popen('xsel').read()
        self.app.session.login_server()
        driver.find_element_by_xpath("//div[@kp-icon-svg='settings-20']").click()
        driver.find_element_by_link_text("Сеть").click()
        driver.find_element_by_link_text("Облака").click()
        if len(driver.find_elements_by_xpath("//tr")) > 0:
            driver.find_element_by_xpath("//button[@name='del0']").click()
            driver.find_element_by_xpath("//button[@ng-click='confirm()']").click()
        ActionChains(driver).pause(0.3).perform()
        driver.find_element_by_xpath("//a[@ng-click='createCloudRequest()']").click()
        driver.find_element_by_xpath("//input[@type='url']").send_keys(vpnlink)
        driver.find_element_by_xpath("(//button[1])[1]").click()
        ActionChains(driver).pause(0.3).perform()
        enablesynch = driver.find_element_by_xpath("//input[@ng-model='model.is_sync_enabled']")
        ActionChains(driver).move_to_element(enablesynch).click(enablesynch).perform()
        driver.find_element_by_xpath("//button[@ng-click='confirm()']").click()
        driver.get("https://172.20.9.134/#!/login")
        self.app.session.open_servs_view()

    def get_servs_list(self):
        driver = self.app.driver
        self.app.session.being_on_servs_page()
        servslist = []
        for element in driver.find_elements_by_xpath("//tr[@class='ng-scope']"):
            text = element.text
            servslist.append(text)
        return len(servslist)
