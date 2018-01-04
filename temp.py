            time.sleep(0.1)
            driver.find_element_by_xpath("//input[@type='text']").send_keys(email)
            driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
            driver.find_element_by_xpath("//input[@value='Log In']").click()

            #time.sleep(0.1)
            driver.find_element_by_css_selector("div.toolbar-icon-container-item.ng-scope > svg.kp-u-icon").click()
            driver.find_element_by_link_text(u"Выйти").click()

            #time.sleep(0.1)
            driver.find_element_by_xpath("//input[@type='text']").send_keys(phone)
            driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
            driver.find_element_by_xpath("//input[@value='Log In']").click()

            #time.sleep(0.1)
            driver.find_element_by_css_selector("div.toolbar-icon-container-item.ng-scope > svg.kp-u-icon").click()
            driver.find_element_by_link_text(u"Выйти").click()
