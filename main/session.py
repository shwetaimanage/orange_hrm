from selenium import webdriver
from main import model as model, elements as element, locators as locator


class create_session(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(300)
        url = model.get_url()
        self.driver.get(url)

    def connect(self):
        try:
            admin_user = model.get_users('admin')
            username = element.find_element(locator.LoginPageLocators.EMAIL_ID, self.driver)
            password = element.find_element(locator.LoginPageLocators.PASSWORD, self.driver)
            login_button = element.find_element(locator.LoginPageLocators.LOGIN, self.driver)
            username.send_keys(admin_user['username'])
            password.send_keys(admin_user['password'])
            login_button.click()
            assert "Welcome Admin" in self.driver.page_source

        except Exception as e:
            print(e,"Failed to login")

        return self.driver
