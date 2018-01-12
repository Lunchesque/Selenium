# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains

class SessionHelper:

    def __init__(self, app):    #инициализация ссылки на создание фикстуры (окружения)
        self.app = app

    def open_station(self):     #переход на указанные url в текущей сессии браузера
        driver = self.app.driver
        driver.get("http://172.20.9.134")   #осуществляется атрибутом класса "webdriver" - ".get("url")"

    def login_as_admin(self):   #логин пользователем в открытой странице из "open_station"
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@type='text']").send_keys("999")  #send_keys - посылает в текстовое поле символы
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admADM1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()    #click - имитация нажатия основной кнопкой мыши на элемент

    def open_organization_page(self):
        driver = self.app.driver
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_xpath("//a[contains(@href, '#!/org/users')]").click()

    def logout(self):
        driver = self.app.driver
        ActionChains(driver).pause(0.05).perform()
        logoutBtn = driver.find_element_by_xpath("(//a[contains(@href, '#')])[20]")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()
