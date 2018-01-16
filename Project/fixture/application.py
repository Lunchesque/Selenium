# -*- coding: utf-8 -*-

from model.data import Data
from selenium import webdriver
from fixture.users import UsersHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.users = UsersHelper(self)

    def is_valid(self):     #прверка, что находимся на необходимой странице (валидация сессии)
        try:
            self.driver.current_url     #путем проверки текущего url на совпадение с необходимым
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
