# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.session.open_station()
    fixture.session.login_as_admin()
    fixture.session.open_organization_page()

    def fin():
        fixture.session.logout()
        fixture.destruction
    request.addfinalizer(fin)
    return fixture
