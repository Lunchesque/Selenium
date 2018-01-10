# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.open_station()
        fixture.session.login_as_admin()
        fixture.session.open_organization_page()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.open_station()
            fixture.session.login_as_admin()
            fixture.session.open_organization_page()
    return fixture

@pytest.fixture(scope = "session", autouse = True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destruction()

    request.addfinalizer(fin)
    return fixture
