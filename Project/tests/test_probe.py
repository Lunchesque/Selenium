# -*- coding: utf-8 -*-
import pytest
from model.data import Data


#@pytest.mark.skip(reason="no way of currently testing this")
def test_probe(app, json_fordel):
    data = json_fordel
    old_users = app.users.get_users_list()
    app.users.creating_users(data)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
