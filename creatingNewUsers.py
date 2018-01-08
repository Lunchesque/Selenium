# -*- coding: utf-8 -*-
import time
import pytest
from Application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destruction)
    return fixture

def test_creating_users(app):      #функция теста, всегда должна начинаться с test_
    index = 0
    app.open_station()
    app.login_as_admin()
    app.open_organization_page()

    while index <= 3:
        time.sleep(0.05)
        app.create_all_types_of_users(index)
        index += 1
    time.sleep(0.1)
    app.logout()
