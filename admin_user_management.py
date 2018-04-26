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

    def test_add_user(self):
        self.click_add_user()
        users_dict = model.users_to_add()
        # add 10 users
        for items in users_dict:
            user_role = Select(element.find_element(locator.UserManagement.USER_ROLE, self.driver))
            user_role.select_by_value(items['User Role'])
            employee_text = element.find_element(locator.UserManagement.EMPLOYEE_NAME, self.driver)
            employee_text.send_keys('a')
            employee_name = element.find_element(locator.UserManagement.EMPLOYEE_NAME_DROPDOWN, self.driver)
            employee_name.click()
            username = element.find_element(locator.UserManagement.USERNAME, self.driver)
            username.send_keys(items['Username'])
            status = Select(element.find_element(locator.UserManagement.STATUS, self.driver))
            status.select_by_visible_text(items['Status'])
            password = element.find_element(locator.UserManagement.PASSWORD, self.driver)
            password.send_keys(items['Password'])
            confirm_password = element.find_element(locator.UserManagement.CONFIRM_PASSWORD, self.driver)
            confirm_password.send_keys(items['Confirm Password'])
            save_button = element.find_element(locator.UserManagement.SAVE_USER_BUTTON, self.driver)
            save_button.click()
            assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/saveSystemUser"
            self.click_add_user()

    def test_delete_users(self):
        delete_user_button = element.find_element(locator.UserManagement.DELETE_USER_BUTTON, self.driver)
        confirm_delete_user_button = element.find_element(locator.UserManagement.CONFIRM_DELETE_USER_BUTTON, self.driver)
        table_id = element.find_element(locator.UserManagement.TABLE_ID, self.driver)
        rows = table_id.find_elements(By.TAG_NAME, 'tr')
        no_of_rows = len(rows)
        if no_of_rows > 2:
            for row in rows[2:3]:
                col = row.find_elements_by_tag_name('td')[0]
                col.click()
                delete_user_button.click()
                confirm_delete_user_button.click()
        else:
            unittest.skip("No Records to delete")

    def get_table_length(self):
        table_id = element.find_element(locator.UserManagement.TABLE_ID, self.driver)
        rows = table_id.find_elements(By.TAG_NAME, 'tr')
        no_of_rows = len(rows)
        return no_of_rows-1

    def test_search_users(self):

        # search based on username
        users_dict = model.users_to_add()
        username_search_field = element.find_element(locator.UserManagement.SEARCH_USERNAME, self.driver)
        username_search_field.send_keys(users_dict[0]['Username'])
        search_button = element.find_element(locator.UserManagement.SEARCH_BUTTON, self.driver)
        search_button.click()
        assert self.get_table_length()== 1

        # search based on User Role
        reset_search = element.find_element(locator.UserManagement.RESET_SEARCH, self.driver)
        reset_search.click()
        for roles in ["ESS", "Admin"]:
            username_search_field = Select(element.find_element(locator.UserManagement.SEARCH_USER_ROLE, self.driver))
            username_search_field.select_by_visible_text(roles)
            search_button = element.find_element(locator.UserManagement.SEARCH_BUTTON, self.driver)
            search_button.click()
            table_id = element.find_element(locator.UserManagement.TABLE_ID, self.driver)
            rows = table_id.find_elements(By.TAG_NAME, 'tr')
            for row in rows[1:]:
                col = row.find_elements_by_tag_name('td')[2]
                assert col.text == roles

        # search based on Employee Name
        reset_search = element.find_element(locator.UserManagement.RESET_SEARCH, self.driver)
        reset_search.click()
        employee_name_text = element.find_element(locator.UserManagement.SEARCH_EMPLOYEE_NAME, self.driver)
        employee_name_text.send_keys('e')
        employee_name_search = element.find_element(locator.UserManagement.SEARCH_EMPLOYEE_NAME_LIST, self.driver)
        name = employee_name_search.text
        employee_name_search.click()
        search_button = element.find_element(locator.UserManagement.SEARCH_BUTTON, self.driver)
        search_button.click()
        #entered_text = element.find_element(locator.UserManagement.SEARCH_EMPLOYEE_NAME, self.driver).value
        table_id = element.find_element(locator.UserManagement.TABLE_ID, self.driver)
        rows = table_id.find_elements(By.TAG_NAME, 'tr')
        # for row in rows[1:]:
        #     col = row.find_elements_by_tag_name('td')[3]
        #     assert col.text == employee_name_search.text

        # search based on Status
        reset_search = element.find_element(locator.UserManagement.RESET_SEARCH, self.driver)
        reset_search.click()
        for status in ["Enabled","Disabled"]:
            username_search_field = Select(element.find_element(locator.UserManagement.SEARCH_STATUS, self.driver))
            username_search_field.select_by_visible_text(status)
            search_button = element.find_element(locator.UserManagement.SEARCH_BUTTON, self.driver)
            search_button.click()
            table_id = element.find_element(locator.UserManagement.TABLE_ID, self.driver)
            rows = table_id.find_elements(By.TAG_NAME, 'tr')
            for row in rows[1:]:
                col = row.find_elements_by_tag_name('td')[4]
                assert col.text == status

    def tearDown(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
