# -*- coding: utf-8 -*-
from random import choice
from string import digits
from model.data import Data
from selenium import webdriver
from fixture.users import UsersHelper
from fixture.session import SessionHelper




class Appliaction:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.users = UsersHelper(self)

    def open_station(self):
        driver = self.driver
        driver.get("https://172.20.9.134/#!/login")

    def destroy(self):
        self.driver.quit()
