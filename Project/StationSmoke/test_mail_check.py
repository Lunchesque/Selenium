import pytest

@pytest.mark.run(order = 3)
def test_mail_check(app, json_mailcheck):
    data = json_mailcheck
    old_users = app.users.get_users_list()
    app.users.creating_for_mail(data)
    #assert len(old_users) + 1 == len(app.users.get_users_list())
    new_users = app.users.get_users_list()
    app.users.mail_check()
