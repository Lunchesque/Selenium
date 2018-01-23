# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data
from TestData.add_user import testdata

@pytest.mark.parametrize("data", testdata, ids = [repr(x) for x in testdata])
def test_probe(app, data):
    old_users = app.users.get_users_list()
    app.users.creating_users(data)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
