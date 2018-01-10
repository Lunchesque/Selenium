# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application
from selenium.webdriver.common.action_chains import ActionChains

def test_creating_users(app):      #функция теста, всегда должна начинаться с test_
    index = 0
    while index <= 3:
        ActionChains(app.driver).pause(0.05).perform()
        app.create_all_types_of_users(index)
        index += 1

    ActionChains(app.driver).pause(0.05).perform()

def test_deleting_auto_users(app):
    app.deletion_circle()
    ActionChains(app.driver).pause(0.05).perform()
