# -*- coding: utf-8 -*-
import json
from model.data import Data
from fixture import application
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class PlacesHelper:

    def __init__(self, app):
        self.app = app

    def create_new_place(self, data):
        driver = self.app.driver
        driver.find_element_by_xpath("(//li/a)[3]").click()
        driver.find_element_by_xpath("(//button)[3]").click()
        driver.find_element_by_xpath("//input[@name='_name']").send_keys(data.placeId.format(data.placeId))
        driver.find_element_by_xpath("(//li[2])[1]").click()
        Select(driver.find_element_by_name("localserver_id")).select_by_index(1)
        driver.find_element_by_xpath("(//button[1])[5]").click()
