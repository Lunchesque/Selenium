# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data


def test_creating_admin(app):
    old_users = app.users.get_users_list()
    creds = Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",userId = (''.join(choice(digits) for i in range(5))),
                                                                                    phone = (''.join(choice(digits) for i in range(15))))
    app.users.creating_admin(creds)
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()

def test_creting_operator(app):
    old_users = app.users.get_users_list()
    app.users.creating_operator(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()



def test_creating_watcher(app):
    old_users = app.users.get_users_list()
    app.users.creating_watcher(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()



def test_creating_demo(app):
    old_users = app.users.get_users_list()
    app.users.creating_demo(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()
