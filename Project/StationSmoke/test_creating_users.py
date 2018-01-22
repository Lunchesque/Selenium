# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data

testdata = [
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 2),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 1),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 0)
]

@pytest.mark.parametrize("data", testdata, ids = [repr(x) for x in testdata])
@pytest.mark.run(order = 2)
def test_creating_users(app, data):
    old_users = app.users.get_users_list()
    app.users.creating_users(data)
    assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
