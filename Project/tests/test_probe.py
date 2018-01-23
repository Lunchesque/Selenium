# -*- coding: utf-8 -*-
from model.data import Data
import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_probe(app, data_fordel):
    data = data_fordel
    old_users = app.users.get_users_list()
    app.users.creating_users(data)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
