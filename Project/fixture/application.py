# -*- coding: utf-8 -*-

from fixture.clouds import CloudsHelper 
from model.data import Data
from selenium import webdriver
from fixture.users import UsersHelper
from fixture.places import PlacesHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url, gmail):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.users = UsersHelper(self)
        self.places = PlacesHelper(self)
        self.clouds = CloudsHelper(self)
        self.base_url = base_url
        self.gmail = gmail

    def is_valid(self):     #прверка, что находимся на необходимой странице (валидация сессии)
        try:
            self.driver.current_url     #путем проверки текущего url на совпадение с необходимым
            return True
        except:
            return False

    def open_station(self):
        driver = self.driver
        driver.get(self.base_url)

    def destroy(self):
        self.driver.quit()
