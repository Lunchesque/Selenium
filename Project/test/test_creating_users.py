# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application
from selenium.webdriver.common.action_chains import ActionChains


def test_creating_users(app):      #функция теста, всегда должна начинаться с test_
    app.create_all_types_of_users()
    ActionChains(app.driver).pause(0.05).perform()
