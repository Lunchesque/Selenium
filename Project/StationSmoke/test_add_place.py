import pytest

@pytest.mark.run(order = 4)
def test_add_place(app, json_places):
    data = json_places
    app.places.create_new_place(data)
