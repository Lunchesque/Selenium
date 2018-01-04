# -*- coding: utf-8 -*-
import time, unittest
from selenium import webdriver
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
        self.driver.implicitly_wait(5)      #устанавливается неяное ожиданиепоявления элементов
        self.driver.maximize_window()       #окно разворачивается на весь экран

    def test_creating_users(self):      #функция теста, всегда должна начинаться с test_

        driver = self.driver    #подключем драйвер к тестовому сценарию
        driver.get("http://172.20.9.134")   #get - переход по url адресу
        wait = WebDriverWait(driver, 10)

        index = 0   #переменная счетчика

        while index <= 3:   #основной цикл теста

            time.sleep(0.1)     #ожидание 0.1 секунды, для прогрузки всех элементов на странице после инициализации драйвера
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).send_keys("999")
            driver.find_element_by_xpath("//input[@type='password']").send_keys("admADM1/")
            driver.find_element_by_xpath("//input[@value='Log In']").click()

            driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
            driver.find_element_by_xpath("//a[contains(@href, '#!/org/users')]").click()

            wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[4]"))).click()

            select = Select(driver.find_element_by_name("role")).select_by_index(index)

            role = driver.find_element_by_name("role").get_attribute("value")
            userId = (''.join(choice(digits) for i in range(5)))
            email = ("AutoTestUser_{0}_{1}@ki.ki".format(role, userId))
            phone = (''.join(choice(digits) for i in range(15)))
            fullName = ("Auto.test.user_{0}_{1}".format(role, userId))
            password = fullName

            wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
            driver.find_element_by_name("phone").send_keys(phone)
            driver.find_element_by_name("fullName").send_keys(fullName)

            driver.find_element_by_name("autoGeneratePassword").click()
            driver.find_element_by_name("showPasswords").click()

            driver.find_element_by_name("password").send_keys(password)
            driver.find_element_by_name("password_confirmation").send_keys(password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[3]"))).click()

            wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href, '#')])[20]"))).click()
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, u"Выйти"))).click()

            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).send_keys(email)
            driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
            driver.find_element_by_xpath("//input[@value='Log In']").click()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.toolbar-icon-container-item.ng-scope > svg.kp-u-icon"))).click()
            driver.find_element_by_link_text(u"Выйти").click()

            time.sleep(0.1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).send_keys(phone)
            driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
            driver.find_element_by_xpath("//input[@value='Log In']").click()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.toolbar-icon-container-item.ng-scope > svg.kp-u-icon"))).click()
            driver.find_element_by_link_text(u"Выйти").click()

            print(" ")
            print("User's role: " + role)
            print("User's email: " + email)
            print("User's phone: " + phone)
            print("User's password: " + password)

            index += 1
            print(index)

    def tearDown(self):

        time.sleep(1)
        self.driver.close()

if __name__ == '__main__':

    unittest.main()
