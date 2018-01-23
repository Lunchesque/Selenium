# -*- coding: utf-8 -*-
import pytest
from model.data import Data
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    if fixture is None:
        fixture = Application(browser = browser, base_url = base_url)
        fixture.open_station()
        fixture.session.login_as_admin(userName = "999", admPass = "admADM1/")
    else:
        if not fixture.is_valid():
            fixture = Application(browser = browser, base_url = base_url)
            fixture.open_station()
            fixture.session.login_as_admin(userName = "999", admPass = "admADM1/")
    return fixture

@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome")
    parser.addoption("--url", action = "store", default = "https://172.20.9.134/#!/login")
