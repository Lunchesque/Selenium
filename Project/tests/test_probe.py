# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data
from TestData.add_user import stationSmokeData

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize("data", stationSmokeData, ids = [repr(x) for x in stationSmokeData])
def test_probe(app, data):
    old_users = app.users.get_users_list()
    app.users.creating_users(data)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
