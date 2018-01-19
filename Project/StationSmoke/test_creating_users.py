# -*- coding: utf-8 -*-
import pytest
from random import choice
from string import digits
from model.data import Data

def test_creating_users(app):
    credsOper = Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
                                                                                        phone = (''.join(choice(digits) for i in range(15))))
    app.users.creating_operator(credsOper)
