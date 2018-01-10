# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application
from selenium.webdriver.common.action_chains import ActionChains

def test_deleting_auto_users(app):
    app.deletion_circle()
    ActionChains(app.driver).pause(0.05).perform()
