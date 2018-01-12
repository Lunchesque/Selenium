# -*- coding: utf-8 -*-

from random import choice
from string import digits
from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Application:

    def __init__(self):     #иницифализия окружения
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.driver.maximize_window()

    def is_valid(self):     #прверка, что находимся на необходимой странице (валидация сессии)
        try:
            self.driver.current_url     #путем проверки текущего url на совпадение с необходимым
            return True
        except:
            return False

    def create_all_types_of_users(self):    #создание пользователей всех ролей
        driver = self.driver
        index = 0       #переменная для выбора номера роли из выпадающего списка
        while index <= 3:   #основной цикл создания пользователей
            addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")  #нахождение кнопки создания добавления пользователей
            ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()    #наведение курсора на кнопку добавления
            Select(driver.find_element_by_name("role")).select_by_index(index)      #выбор роли пользователя, индекс - номер в выпадающем списке

            role = driver.find_element_by_name("role").get_attribute("value")   #занесение в переменную значение поля "Роль"
            userId = (''.join(choice(digits) for i in range(5)))    #генерация уникального рандомного идентификатора пользователя
            email = ("AutoTestUser_{0}_{1}@ki.ki".format(role, userId))     #генерация валидного email для пользователя с использованием значения роли и уникального идентификатора
            phone = (''.join(choice(digits) for i in range(15)))    #генерация рандомного телефонного номера пользователя
            fullName = ("Auto.test.user_{0}_{1}".format(role, userId))  #генерация валидного имени пользователя с использованием значения роли и уникального идентификатора
            password = fullName     #пароль равен имени пользователя
            #send_keys - вписание значений в поля
            driver.find_element_by_name("email").send_keys(email)
            driver.find_element_by_name("phone").send_keys(phone)
            driver.find_element_by_name("fullName").send_keys(fullName)

            driver.find_element_by_name("autoGeneratePassword").click()     #деактивация чекбокса автогенераци пароля
            driver.find_element_by_name("showPasswords").click()    #активация чекбокса показать пароли
            #вписание пароля в поля "Пароль" и "Подтвеждение пароля"
            driver.find_element_by_name("password").send_keys(password)
            driver.find_element_by_name("password_confirmation").send_keys(password)
            #нажатие на кнопку "Создать"
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            index += 1
            ActionChains(driver).pause(0.05).perform()

    def deletion_auto_users(self):
        driver = self.driver
        a = 1   #индекс строки
        autoNum = driver.find_elements_by_xpath("(//tr/td/span[contains(@title, 'Auto.test.user')])")   #забор спписка автоматически созданных пользователей
        count = len(autoNum)    #нахождение длинны этого списка
        if count != 0:  #если длинна списка автопользователей не равно 0, начинается цикл по поиску номера первого автопользователя
            while count != 0:
                #нахождение имени пользователят в строке с индексом "а"
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

    def destruction(self):  #закрытие окна браузера
        self.driver.quit()
