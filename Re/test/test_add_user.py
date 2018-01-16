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

def test_untitled_test_case(app):
    app.user_login(userName = "999", admPass = "admADM1/")
    app.creating_admin(Data(email = "AutoTestUser_{0}@ki.ki", name = "Auto.test.user_{0}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
