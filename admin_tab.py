import locators as locator
import elements as element
import session


class admin_tab():
    def __init__(self):
        session_object = session.create_session()
        self.driver = session_object.connect()

    def get_user_management(self):
        add_button = element.find_element(locator.Admin.CLICK_ADMIN, self.driver)
        add_button.click()
        assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
        users = element.find_element(locator.Admin.USERS, self.driver)

        return self.driver