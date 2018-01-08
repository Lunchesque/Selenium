# -*- coding: utf-8 -*-
import time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DeletingTestUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open_station(self):
        driver = self.driver
        driver.get("http://172.20.9.134")

    def login_as_admin(self):
        driver = self.driver
        driver.find_element_by_xpath("//input[@type='text']").send_keys("999")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admADM1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()

    def open_organization_page(self):
        driver = self.driver
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_xpath("//a[contains(@href, '#!/org/users')]").click()

    def deletion_auto_users(self):
        driver = self.driver
        optionsBtn = driver.find_element_by_xpath("(//button[@type='button'])[6]")
        ActionChains(driver).move_to_element(optionsBtn).click(optionsBtn).perform()
        driver.find_element_by_link_text(u"Удалить").click()
        driver.find_element_by_xpath("//div[3]/button[contains(@class, 'primary')]").click()

    def test_deleting(self):
        driver = self.driver
        self.open_station()
        self.login_as_admin()
        self.open_organization_page()

        deletion = True
        title = driver.find_element_by_xpath("(//tr/td/span[contains(@ng-bind, 'user')])[1]").get_attribute("title")
        while deletion:
            print(title)
            if "Auto.test.user_" in title:
                self.deletion_auto_users()
                time.sleep(0.05)
            else:
                print("No AutoTestUsers Found")
                deletion = False
            title = driver.find_element_by_xpath("(//tr/td/span[contains(@ng-bind, 'user')])[1]").get_attribute("title")

    def tearDown(self):
        time.sleep(0.5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
