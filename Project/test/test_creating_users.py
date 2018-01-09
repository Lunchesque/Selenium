# -*- coding: utf-8 -*-

import time
import pytest
from fixture.Application import Application
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destruction)
    return fixture

def test_creating_users(app):      #функция теста, всегда должна начинаться с test_
    index = 0
    app.session.open_station()
    app.session.login_as_admin()
    app.open_organization_page()

    while index <= 3:
        #time.sleep(0.05)
        ActionChains(app.driver).pause(0.05).perform()
        app.create_all_types_of_users(index)
        index += 1
    #time.sleep(0.1)
    ActionChains(app.driver).pause(0.05).perform()
    app.session.logout()
