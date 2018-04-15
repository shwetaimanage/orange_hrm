from selenium.webdriver.common.by import By
import unittest
import locators as locator
import elements as element
import admin_tab, model
from selenium.webdriver.support.ui import Select

class user_management(unittest.TestCase):
    @classmethod
    def setUp(cls):
        session_object = admin_tab.admin_tab()
        cls.driver = session_object.get_user_management()

    def click_add_user(self):
        add_button = element.find_element(locator.Admin.ADD_BUTTON, self.driver)
        add_button.click()
        assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/saveSystemUser"

    # def test_add_user(self):
    #     self.click_add_user()
    #     users_dict = model.users_to_add()
    #     # add 10 users
    #     for items in users_dict:
    #         user_role = Select(element.find_element(locator.UserManagement.USER_ROLE, self.driver))
    #         user_role.select_by_value(items['User Role'])
    #         employee_name = element.find_element(locator.UserManagement.EMPLOYEE_NAME, self.driver)
    #         employee_name.send_keys(items['Employee Name'])
    #         username = element.find_element(locator.UserManagement.USERNAME, self.driver)
    #         username.send_keys(items['Username'])
    #         status = Select(element.find_element(locator.UserManagement.STATUS, self.driver))
    #         status.select_by_visible_text(items['Status'])
    #         password = element.find_element(locator.UserManagement.PASSWORD, self.driver)
    #         password.send_keys(items['Password'])
    #         confirm_password = element.find_element(locator.UserManagement.CONFIRM_PASSWORD, self.driver)
    #         confirm_password.send_keys(items['Confirm Password'])
    #         save_button = element.find_element(locator.UserManagement.SAVE_USER_BUTTON, self.driver)
    #         save_button.click()
    #         assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/saveSystemUser"
    #         self.click_add_user()

    def test_delete_users(self):
        table_id = element.find_element(locator.UserManagement.TABLE_ID, self.driver)
        rows = table_id.find_elements(By.TAG_NAME, 'tr')
        for row in rows[1:]:
            col = row.find_elements_by_tag_name('td')[1]
            print col.text
            break


    def search_users(self):
        pass

    def tearDown(cls):
        cls.driver.close()
        pass


if __name__ == "__main__":
    unittest.main()
