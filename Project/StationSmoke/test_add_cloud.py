import pytest

@pytest.mark.run(order = 5)
def test_add_cloud(app):
    app.clouds.add_cloud()
    assert app.clouds.get_servs_list() > 0
