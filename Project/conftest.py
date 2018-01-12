# -*- coding: utf-8 -*-

import pytest
from fixture.Application import Application     #импорт модуля с вспомогательными функциями

fixture = None      #присвоение фикстуре пустого значения

@pytest.fixture     #такая запись дает понять pytest что это конфигурация фикстуры
def app(request):   #функция обавления фикстуры для тестов
    global fixture      #такая запись позволяет использовать глобальную переменную для фикстуры
    if fixture is None:     #если значение фиксуры пустое
        fixture = Application()     #то происходит ее создание
        fixture.session.open_station()      #с параметрами сессии для запускаемых тестов
        fixture.session.login_as_admin()
        fixture.session.open_organization_page()
    else:       #проверка, если сессия была закрыта, разрушена или недоступна
        if not fixture.is_valid():      #если у сессии не тот url, который был задан при инициализации
            fixture = Application()         #создается ноная фикструа и сессия, чтобы пройти оставшиеся тесты
            fixture.session.open_station()
            fixture.session.login_as_admin()
            fixture.session.open_organization_page()
    return fixture

@pytest.fixture(scope = "session", autouse = True)  #scope = "session" - определение фикстуры(вспомогательных фунций) для всей сессии
                                                    #фикстура завершения сессии после окончания всех тестов, а не после каждого отдельного
                                                    #под сессией понимается открытое окно браузера
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destruction()

    request.addfinalizer(fin)
    return fixture
