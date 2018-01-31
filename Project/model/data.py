# -*- coding: utf-8 -*-

class Data:

    def __init__(self, email = None, name = None, userId = None, phone = None, role = None, placeId = None):
        self.email = email
        self.name = name
        self.userId = userId
        self.phone = phone
        self.role = role
        self.placeId = placeId


    def __repr__(self):
        return "%s_%s_%s" % (self.name, self.userId, self.phone)

    def __eq__(self, other):
        return self.name == other.name
