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

def test_creating_admin(app):
    app.session.login_as_admin(userName = "999", admPass = "admADM1/")
    app.users.creating_admin(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    app.session.logout()


def test_creting_operator(app):
    app.session.login_as_admin(userName = "999", admPass = "admADM1/")
    app.users.creating_operator(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    app.session.logout()

def test_creating_watcher(app):
    app.session.login_as_admin(userName = "999", admPass = "admADM1/")
    app.users.creating_watcher(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    app.session.logout()

def test_creating_demo(app):
    app.session.login_as_admin(userName = "999", admPass = "admADM1/")
    app.users.creating_demo(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    app.session.logout()
