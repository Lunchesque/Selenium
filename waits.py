# -*- coding: utf-8 -*-
import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitsTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("http://172.20.9.134")

    def test_waits(self):

        driver = self.driver
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))).send_keys("999")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))).send_keys("admADM1/")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Log In']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href, '#')])[14]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#!/org/users')]"))).click()

    def tearDown(self):

        time.sleep(1)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
