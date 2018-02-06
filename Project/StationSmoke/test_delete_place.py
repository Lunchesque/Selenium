# -*- coding: utf-8 -*-
import pytest



#@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order = 5)
def test_deleting_auto_places(app):
    app.places.deletion_auto_places()
