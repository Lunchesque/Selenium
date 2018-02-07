import pytest

#@pytest.mark.run(order = 7)
def test_choosing_places(app):
    app.places.choosing_places()
