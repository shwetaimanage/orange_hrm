from selenium import webdriver
import unittest
import model as model
import locators as locator
import elements as element

class test_home_page(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(300)
        url = model.get_url()
        cls.driver.get(url)

    def test_links(self):
        web_link= self.driver.find_element_by_xpath('//*[@id="footer"]/div[1]/a')
        web_link.click()
        self.assertEqual(" HR Management System | OrangeHRM l HR Management Software ", self.driver.title)
        self.driver.back()
        # linkedin_link = self.driver.find_element_by_xpath('//*[@id="social-icons"]/a[1]')
        # linkedin_link.click()
        # self.assertIn("OrangeHRM - World's Most Popular Opensource HRIS - Home", self.driver.page_source)
        # self.driver.back()
        # facebook_link = self.driver.find_element_by_xpath('//*[@id="social-icons"]/a[2]')
        # facebook_link.click()
        # self.assertIn("OrangeHRM - World's Most Popular Opensource HRIS - Home", self.driver.page_source)
        # self.driver.back()
        # twitter_link = self.driver.find_element_by_xpath('//*[@id="social-icons"]/a[3]')
        # twitter_link.click()
        # self.assertIn("OrangeHRM Inc. (@orangehrm) | Twitter", self.driver.page_source)
        # self.driver.back()
        # youtube_link = self.driver.find_element_by_xpath('//*[@id="social-icons"]/a[4]')
        # youtube_link.click()
        # self.assertIn("Youtube", self.driver.page_source)
        # self.driver.back()


    def test_login(self):
        self.assertIn("OrangeHRM", self.driver.title)
        admin_user= model.get_users('admin')
        username=element.find_element(locator.LoginPageLocators.EMAIL_ID, self.driver)
        password= element.find_element(locator.LoginPageLocators.PASSWORD, self.driver)
        login_button=element.find_element(locator.LoginPageLocators.LOGIN,self.driver)
        username.send_keys(admin_user['username'])
        password.send_keys(admin_user['password'])
        login_button.click()
        assert "Welcome Admin" in self.driver.page_source

    def tearDown(cls):
        #cls.driver.close()
        pass


if __name__ == "__main__":
    unittest.main()
