    def open_station(self, driver):
        driver.get("http://172.20.9.134")

    def login_as_admin(self, driver):
        driver.find_element_by_xpath("//input[@type='text']").send_keys("999")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("admADM1/")
        driver.find_element_by_xpath("//input[@value='Log In']").click()

    def open_organization_page(self, driver):
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[14]").click()
        driver.find_element_by_xpath("//a[contains(@href, '#!/org/users')]").click()

from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).pause(0.3).perform()


(//tr/td/span[contains(@ng-bind, 'user')])[1]
