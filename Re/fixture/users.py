# -*- coding: utf-8 -*-
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class UsersHelper:

    def __init__(self, app):
        self.app = app

    def open_users_list(self):
        driver = self.app.driver
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_link_text(u"Пользователи").click()

    def creating_admin(self, data):
        driver = self.app.driver
        self.open_users_list()

        addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")  #нахождение кнопки создания добавления пользователей
        ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()    #наведение курсора на кнопку добавления
        Select(driver.find_element_by_name("role")).select_by_index(3)      #выбор роли пользователя, индекс - номер в выпадающем списке

        role = driver.find_element_by_name("role").get_attribute("value")

        driver.find_element_by_name("email").send_keys(data.email.format(role, data.userId))
        driver.find_element_by_name("phone").send_keys(data.phone)
        driver.find_element_by_name("fullName").send_keys(data.name.format(role, data.userId))

        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()
        driver.find_element_by_name("password").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_name("password_confirmation").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_name("enableNotifications").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        ActionChains(driver).pause(0.05).perform()

    def creating_operator(self, data):
        driver = self.app.driver
        self.open_users_list()

        addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")  #нахождение кнопки создания добавления пользователей
        ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()    #наведение курсора на кнопку добавления
        Select(driver.find_element_by_name("role")).select_by_index(2)      #выбор роли пользователя, индекс - номер в выпадающем списке

        role = driver.find_element_by_name("role").get_attribute("value")

        driver.find_element_by_name("email").send_keys(data.email.format(role, data.userId))
        driver.find_element_by_name("phone").send_keys(data.phone)
        driver.find_element_by_name("fullName").send_keys(data.name.format(role, data.userId))

        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()
        driver.find_element_by_name("password").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_name("password_confirmation").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        ActionChains(driver).pause(0.05).perform()

    def creating_watcher(self, data):
        driver = self.app.driver
        self.open_users_list()

        addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")  #нахождение кнопки создания добавления пользователей
        ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()    #наведение курсора на кнопку добавления
        Select(driver.find_element_by_name("role")).select_by_index(1)      #выбор роли пользователя, индекс - номер в выпадающем списке

        role = driver.find_element_by_name("role").get_attribute("value")

        driver.find_element_by_name("email").send_keys(data.email.format(role, data.userId))
        driver.find_element_by_name("phone").send_keys(data.phone)
        driver.find_element_by_name("fullName").send_keys(data.name.format(role, data.userId))

        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()
        driver.find_element_by_name("password").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_name("password_confirmation").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        ActionChains(driver).pause(0.05).perform()

    def creating_demo(self, data):
        driver = self.app.driver
        self.open_users_list()

        addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")  #нахождение кнопки создания добавления пользователей
        ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()    #наведение курсора на кнопку добавления
        Select(driver.find_element_by_name("role")).select_by_index(0)      #выбор роли пользователя, индекс - номер в выпадающем списке

        role = driver.find_element_by_name("role").get_attribute("value")

        driver.find_element_by_name("email").send_keys(data.email.format(role, data.userId))
        driver.find_element_by_name("phone").send_keys(data.phone)
        driver.find_element_by_name("fullName").send_keys(data.name.format(role, data.userId))

        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()
        driver.find_element_by_name("password").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_name("password_confirmation").send_keys(data.name.format(role, data.userId))
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        ActionChains(driver).pause(0.05).perform()


    def deletion_auto_users(self):
        driver = self.app.driver
        self.open_users_list()
        a = 1
        autoNum = driver.find_elements_by_xpath("(//tr/td/span[contains(@title, 'Auto.test.user')])")
        count = len(autoNum)
        if count != 0:
            while count != 0:
                title = driver.find_element_by_xpath("(//span[contains(@ng-bind, 'full_name')])[{}]".format(a)).get_attribute("title")
                if "Auto.test.user" in title:   #если имя в имени пользователя есть "Auto.test.user", то начинается удаление
                    btnNum = 5 + a      #индекс кнопки опции на странице для найденнгого пользователя
                    optionsBtn = driver.find_element_by_xpath("(//button[@type='button'])[{}]".format(btnNum))  #нахождение кнопки опции на странице для найденнгого пользователя
                    ActionChains(driver).move_to_element(optionsBtn).click(optionsBtn).perform()    #перемещение курсора на эту кнопку, чтобы сделать видимой, и нажатие
                    driver.find_element_by_link_text(u"Удалить").click()    #выбор из выпадающего списка удаление и нажатие
                    driver.find_element_by_xpath("//div[3]/button[contains(@class, 'primary')]").click()    #нажать на кнопку подтверждения удаления
                    count -= 1
                    ActionChains(driver).pause(0.05).perform()
                else:   #увеличение счетчика, если в списке не автопользователь
                    a += 1
        else:
            pass
