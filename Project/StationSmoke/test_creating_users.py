# -*- coding: utf-8 -*-
import pytest

from model.data import Data

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order = 2)
def test_creating_users(app, json_statiosmoke):
    data = json_statiosmoke
    old_users = app.users.get_users_list()
    app.users.creating_users(data)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
