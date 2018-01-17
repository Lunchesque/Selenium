# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data


def test_creating_admin(app):
    old_users = app.users.get_users_list()
    app.users.creating_admin(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    new_users = app.users.get_users_list()
    assert len(old_users) + 1 == len(new_users)

def test_creting_operator(app):
    old_users = app.users.get_users_list()
    app.users.creating_operator(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    new_users = app.users.get_users_list()
    assert len(old_users) + 1 == len(new_users)



def test_creating_watcher(app):
    old_users = app.users.get_users_list()
    app.users.creating_watcher(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    new_users = app.users.get_users_list()
    assert len(old_users) + 1 == len(new_users)



def test_creating_demo(app):
    old_users = app.users.get_users_list()
    app.users.creating_demo(Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}",
                                    userId = (''.join(choice(digits) for i in range(5))),
                                    phone = (''.join(choice(digits) for i in range(15)))))
    new_users = app.users.get_users_list()
    assert len(old_users) + 1 == len(new_users)
