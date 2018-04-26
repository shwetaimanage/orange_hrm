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
        element.find_element(locator.Admin.USERS, self.driver)
        return self.driver

    def get_job(self, page_name):
        add_button = element.find_element(locator.Admin.CLICK_ADMIN, self.driver)
        add_button.click()
        job_tab = element.find_element(locator.Job.JOB_TAB, self.driver)
        job_tab.click()
        assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/viewSystemUsers#"
        if page_name == 'JOB_TITTLE':
            tab=element.find_element(locator.Job.JOB_TITTLE, self.driver)
            tab.click()
            assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
            return self.driver
        elif page_name == 'PAY_GRADES':
            tab=element.find_element(locator.Job.PAY_GRADES, self.driver)
            tab.click()
            assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/viewPayGrades"
            return self.driver
        elif page_name == 'EMPLOYEMENT_STATUS':
            tab=element.find_element(locator.Job.EMPLOYEMENT_STATUS, self.driver)
            tab.click()
            assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/employmentStatus"
            return self.driver
        elif page_name == 'JOB_CATEGORIES':
            tab=element.find_element(locator.Job.JOB_CATEGORIES, self.driver)
            tab.click()
            assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/jobCategory"
            return self.driver
        elif page_name == 'WORK_SHIFTS':
            tab=element.find_element(locator.Job.WORK_SHIFTS, self.driver)
            tab.click()
            assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/workShift"
            return self.driver



