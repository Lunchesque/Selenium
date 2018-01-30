# -*- coding: utf-8 -*-
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order = 1)
def test_login_as_admin(app):
    app.users.admin_logged_validation()
