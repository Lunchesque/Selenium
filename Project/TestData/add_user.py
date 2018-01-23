# -*- coding: utf-8 -*-
from random import choice
from string import digits
from model.data import Data


stationSmokeData = [
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 2),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 1),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 0)
]

addAllUsersData = [
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 3),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 2),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 1),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 0)
]


del_data = [
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 0)
]
