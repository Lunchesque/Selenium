# -*- coding: utf-8 -*-
import json
from model.data import Data
from fixture import application
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class PlacesHelper:

    def __init__(self, app):
        self.app = app

    def create_new_place(self, data):
        driver = self.app.driver
        self.app.session.being_on_locations_page()
        driver.find_element_by_xpath("(//button)[3]").click()
        driver.find_element_by_xpath("//input[@name='_name']").send_keys(data.name.format(data.placeId))
        driver.find_element_by_xpath("(//li[2])[1]").click()
        Select(driver.find_element_by_name("localserver_id")).select_by_index(1)
        ActionChains(driver).pause(0.1).perform()
        driver.find_element_by_xpath("//button[@ng-click='$ctrl.save()']").click()
        ActionChains(driver).pause(0.2).perform()

    def deletion_auto_places(self):
        driver = self.app.driver
        self.app.session.being_on_locations_page()
        a = 1
        count = self.count()
        if count != 0:
            while count != 0:
                try:
                    title = driver.find_element_by_xpath("(//div[contains(@class, 'location-name')])[{}]".format(a)).get_attribute("title")
                except NoSuchElementException:
                    pass
                if "Auto.test" in title:   #если имя в имени пользователя есть "Auto.test.user", то начинается удаление
                    doc = driver.find_element_by_xpath("(//div[contains(@class, 'location-name')])[{}]".format(a))
                    ActionChains(driver).move_to_element(doc).perform()
                    driver.find_element_by_xpath("(//button[contains(@class, 'btn dots-menu')])[{}]".format(a)).click()
                    driver.find_element_by_link_text(u"Удалить").click()
                    driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
                    count -= 1
                    ActionChains(driver).pause(0.1).perform()
                elif self.get_places() < a:
                    break
                else:   #увеличение счетчика, если в списке не автопользователь
                    a += 1
        else:
            pass

    def choosing_places(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("div.pull-left.locations-dropdown-title").click()
        locations = driver.find_element_by_xpath("//div[contains(@class, 'pull')]").click()

        ActionChains(driver).pause(2).perform()
        driver.find_element_by_xpath("(//a[contains(@href, '')])[6]").click()
        driver.find_element_by_xpath("(//li/a)[3]").click()
        driver.find_element_by_xpath("//div[4]/div[2]/div").click()

    def get_places(self):
        driver = self.app.driver
        allplaces = driver.find_elements_by_xpath("//li[@class='sidebar-list__item ng-scope']")
        return len(allplaces)

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath("//div[contains(@title, 'Auto.test.place')]"))
