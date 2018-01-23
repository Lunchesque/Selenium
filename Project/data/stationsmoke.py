# -*- coding: utf-8 -*-
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
