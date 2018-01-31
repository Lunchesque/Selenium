# -*- coding: utf-8 -*-
import jsonpickle, getopt
import os.path, sys
from random import choice
from string import digits
from model.data import Data



testdata = [
    Data(email = "sergey.verkhovodko+1@synesis.ru", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 3)
]

file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/mailcheck.json")

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))


testdata = [
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 3),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 2),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 1),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 0)
]

file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/allusersdata.json")

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))


testdata = [
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 0)
]

file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/fordel.json")

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))


testdata = [
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 2),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 1),
    Data(email = "AutoTestUser_{}_{}@ki.ki", name = "Auto.test.user_{}_{}", userId = (''.join(choice(digits) for i in range(5))),
            phone = (''.join(choice(digits) for i in range(15))), role = 0)
    ]

file = config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/statiosmoke.json")

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))
