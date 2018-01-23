# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data
from TestData.add_user import del_data


@pytest.mark.parametrize("data", del_data, ids = [repr(x) for x in del_data])
@pytest.mark.run(order = 2)
def test_deleting_auto_users(app, data):
    if app.users.count() == 0:
        app.users.creating_users(data)
    old_users = app.users.get_users_list()
    auto_users = app.users.count()
    app.users.deletion_auto_users()
    assert len(old_users) - auto_users == app.users.count()
    new_users = app.users.get_users_list()
