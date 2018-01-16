# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


def test_deleting_auto_users(app):
    app.users.deletion_auto_users()
