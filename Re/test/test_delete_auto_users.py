# -*- coding: utf-8 -*-
import pytest
from model.data import Data
from random import choice
from string import digits
from fixture.application import Appliaction

@pytest.fixture
def app(request):
    fixture = Appliaction()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_deleting_auto_users(app):
    app.session.login_as_admin(userName = "999", admPass = "admADM1/")
    app.users.deletion_auto_users()
    app.session.logout()
