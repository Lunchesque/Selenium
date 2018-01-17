# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data


def test_deleting_auto_users(app):
    if app.users.count() == 0:
        app.users.creating_demo(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                        userId = (''.join(choice(digits) for i in range(5))),
                                        phone = (''.join(choice(digits) for i in range(15)))))
    old_users = app.users.get_users_list()
    auto_users = app.users.count()
    app.users.deletion_auto_users()
    assert len(old_users) - auto_users == app.users.count()
    new_users = app.users.get_users_list()
