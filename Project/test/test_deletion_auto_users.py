# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application
from selenium.webdriver.common.action_chains import ActionChains

def test_deleting_auto_users(app):
    deletion = True
    app.session.open_station()
    app.session.login_as_admin()
    app.session.open_organization_page()
    app.deletion_circle()
    ActionChains(app.driver).pause(0.05).perform()
    app.session.logout()
