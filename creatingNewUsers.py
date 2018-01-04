# -*- coding: utf-8 -*-
import time, unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random import choice
from string import digits

class TestCreation(unittest.TestCase):

    def setUp(self):    #функция инициализации
        self.driver = webdriver.Chrome()    #инициализируется драйвер для браузера
        self.driver.maximize_window()       #окно разворачивается на весь экран

    def open_station(self, driver):
        driver.get("http://172.20.9.134")

    def login_as_admin(self, driver):
        driver.find_element_by_xpath("//input[@type='text']").send_keys("999")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admADM1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()

    def open_organization_page(self, driver):
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_xpath("//a[contains(@href, '#!/org/users')]").click()

    def create_all_types_of_users(self, driver, index):
        addBtn = driver.find_element_by_xpath("//button[contains(@ng-click, 'create()')]")
        ActionChains(driver).move_to_element(addBtn).click(addBtn).perform()
        select = Select(driver.find_element_by_name("role")).select_by_index(index)

        role = driver.find_element_by_name("role").get_attribute("value")
        userId = (''.join(choice(digits) for i in range(5)))
        email = ("AutoTestUser_{0}_{1}@ki.ki".format(role, userId))
        phone = (''.join(choice(digits) for i in range(15)))
        fullName = ("Auto.test.user_{0}_{1}".format(role, userId))
        password = fullName

        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("phone").send_keys(phone)
        driver.find_element_by_name("fullName").send_keys(fullName)

        driver.find_element_by_name("autoGeneratePassword").click()
        driver.find_element_by_name("showPasswords").click()

        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("password_confirmation").send_keys(password)

        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

        print(" ")
        print("User's role: " + role)
        print("User's email: " + email)
        print("User's phone: " + phone)
        print("User's password: " + password)
        print(index)

    def logout(self, driver):
        logoutBtn = driver.find_element_by_xpath("(//a[contains(@href, '#')])[20]")
        ActionChains(driver).move_to_element(logoutBtn).click(logoutBtn).perform()
        driver.find_element_by_link_text(u"Выйти").click()

    def test_creating_users(self):      #функция теста, всегда должна начинаться с test_

        index = 0
        driver = self.driver
        driver.implicitly_wait(10)  #подключем драйвер к тестовому сценарию
        self.open_station(driver)
        self.login_as_admin(driver)
        self.open_organization_page(driver)

        while index <= 3:
            time.sleep(0.1)
            self.create_all_types_of_users(driver, index)
            index += 1

        self.logout(driver)

    def tearDown(self):
        time.sleep(1)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
