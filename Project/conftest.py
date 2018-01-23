# -*- coding: utf-8 -*-
import pytest, json, os.path
from model.data import Data
from fixture.application import Application

fixture = None
target = None

@pytest.fixture
def app(request):
    global target
    global fixture
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target")) #необходимо тольк для винды
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser = browser, base_url = target["base_url"])
        fixture.open_station()
        fixture.session.login_as_admin(userName = target["userName"], admPass = target["admPass"])
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
    parser.addoption("--target", action = "store", default = "target.json")
