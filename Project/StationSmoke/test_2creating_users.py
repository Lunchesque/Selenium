# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data

def test_creating_users(app):
    credsOper = Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                                            userId = (''.join(choice(digits) for i in range(5))),
                                                            phone = (''.join(choice(digits) for i in range(15))))
    old_users = app.users.get_users_list()
    app.users.creating_operator(credsOper)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()

    credsWatcher = Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                                            userId = (''.join(choice(digits) for i in range(5))),
                                                            phone = (''.join(choice(digits) for i in range(15))))
    old_users = app.users.get_users_list()
    app.users.creating_watcher(credsWatcher)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()

    credsDemo = Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                                            userId = (''.join(choice(digits) for i in range(5))),
                                                            phone = (''.join(choice(digits) for i in range(15))))
    old_users = app.users.get_users_list()
    app.users.creating_demo(credsDemo)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
