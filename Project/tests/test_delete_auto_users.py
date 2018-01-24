# -*- coding: utf-8 -*-
import pytest
from model.data import Data



#@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order = 2)
def test_deleting_auto_users(app, json_fordel):
    data = json_fordel
    if app.users.count() == 0:
        app.users.creating_users(data)
    old_users = app.users.get_users_list()
    auto_users = app.users.count()
    app.users.deletion_auto_users()
    assert len(old_users) - auto_users == app.users.count()
    new_users = app.users.get_users_list()
