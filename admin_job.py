from selenium.webdriver.common.by import By
import unittest
import os

from selenium.webdriver.support.wait import WebDriverWait

import locators as locator
import elements as element
import admin_tab, model
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# class Job_tittle(unittest.TestCase):
#     @classmethod
#     def setUp(cls):
#         session_object = admin_tab.admin_tab()
#         cls.driver = session_object.get_job('JOB_TITTLE')
#
#     def test_all_delete_tittle(self):
#         table_id = element.find_element(locator.Job.JOB_TITTLE_TABLE, self.driver)
#         if "No Records Found" in table_id.text:
#             unittest.skip("No Records to delete")
#         else:
#             heading_row = table_id.find_elements(By.TAG_NAME, 'thead')
#             select_all_columns = heading_row[0].find_elements_by_tag_name('th')[0]
#             select_all_columns.click()
#             delete_tittle = element.find_element(locator.Job.JOB_TITTLE_DELETE, self.driver)
#             delete_tittle.click()
#             confirm_delete = element.find_element(locator.Job.JOB_TITTLE_DELETE_CONFIRMATION, self.driver)
#             confirm_delete.click()
#             table_id = element.find_element(locator.Job.JOB_TITTLE_TABLE, self.driver)
#             assert "No Records Found" in table_id.text
#
#     def test_add_tittle(self):
#         job_tittle_data = model.add_job_tittle()
#         for items in job_tittle_data['tittles']:
#             add_button = element.find_element(locator.Job.JOB_TITTLE_ADD, self.driver)
#             add_button.click()
#             assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/saveJobTitle"
#             job_tittle = element.find_element(locator.Job.ADD_JOB_TITTLE, self.driver)
#             job_tittle.clear()
#             job_tittle.send_keys(items)
#             try:
#                 message = WebDriverWait(self.driver, timeout=0.5).until(EC.visibility_of_element_located(locator.Job.JOB_TITTLE_MESSAGE))
#             except:
#                 pass
#             else:
#                 if message.text == "Already exists":
#                     cancel_button = element.find_element(locator.Job.JOB_TITTLE_CANCEL, self.driver)
#                     cancel_button.click()
#                     continue
#             job_description = element.find_element(locator.Job.JOB_DESCRIPTION, self.driver)
#             job_description.send_keys(job_tittle_data['job_description'])
#             job_specification = element.find_element(locator.Job.JOB_SPECIFICATION, self.driver)
#             job_specification.send_keys(os.getcwd()+"/sample_image.png")
#             job_note = element.find_element(locator.Job.NOTE, self.driver)
#             job_note.send_keys(job_tittle_data['note'])
#             save_job_tittle = element.find_element(locator.Job.SAVE_JOB_TITTLE, self.driver)
#             save_job_tittle.click()
#             assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
#             table_id = element.find_element(locator.Job.JOB_TITTLE_TABLE, self.driver)
#             rows = table_id.find_elements(By.TAG_NAME, 'tr')
#             tittles = []
#             for row in rows[1:]:
#                 col = row.find_elements_by_tag_name('td')[1]
#                 tittles.append(col.text)
#             assert items in tittles
#
#     def test_delete_one_tittle(self):
#         table_id = element.find_element(locator.Job.JOB_TITTLE_TABLE, self.driver)
#         if "No Records Found" in table_id.text:
#             unittest.skip("No Records to delete")
#         else:
#             table_rows = table_id.find_elements(By.TAG_NAME, 'tr')
#             first_row = table_rows[1]
#             initial_row_count = len(table_rows)
#             first_col = first_row.find_elements_by_tag_name('td')[0]
#             checkbox = first_col.find_elements_by_tag_name('input')[0]
#             checkbox.click()
#             delete_tittle = element.find_element(locator.Job.JOB_TITTLE_DELETE, self.driver)
#             delete_tittle.click()
#             confirm_delete = element.find_element(locator.Job.JOB_TITTLE_DELETE_CONFIRMATION, self.driver)
#             confirm_delete.click()
#             table_id = element.find_element(locator.Job.JOB_TITTLE_TABLE, self.driver)
#             row = table_id.find_elements(By.TAG_NAME, 'tr')
#             final_row_count = len(row)
#             assert final_row_count == initial_row_count-1
#
#
#     def tearDown(cls):
#         #cls.driver.close()
#         pass


class Pay_grades(unittest.TestCase):
    flag = False
    @classmethod
    def setUp(cls):
        session_object = admin_tab.admin_tab()
        cls.driver = session_object.get_job('PAY_GRADES')

    @unittest.skipIf(flag == True, "Currency already exists")
    def test_add_pay_grade(self):
        pay_grade_data = model.get_pay_grades()
        add_pay_grades = element.find_element(locator.Job.PAY_GRADES_ADD_BUTTON, self.driver)
        add_pay_grades.click()
        assert self.driver.current_url == "http://opensource.demo.orangehrmlive.com/index.php/admin/payGrade"
        pay_grade_name = element.find_element(locator.Job.PAY_GRADE_ADD_NAME, self.driver)
        pay_grade_name.send_keys(pay_grade_data['name'])
        try:
            message = WebDriverWait(self.driver, timeout=0.5).until(EC.visibility_of_element_located(locator.Job.PAY_GRADES_NAME_MESSAGE))
        except:
            pass
        else:
            if message.text == "Already exists":
                Pay_grades.flag= True
        save_pay_grade = element.find_element(locator.Job.PAY_GRADES_SAVE, self.driver)
        save_pay_grade.click()
        add_currency = element.find_element(locator.Job.ADD_CURRENCY, self.driver)
        add_currency.click()
        table_visible = WebDriverWait(self.driver, timeout=0.05).until(EC.visibility_of_element_located(locator.Job.CURRENCY_TABLE))
        assert table_visible



    def tearDown(cls):
        cls.driver.close()
        pass


# class Employement_status(unittest.TestCase):
#     @classmethod
#     def setUp(cls):
#         session_object = admin_tab.admin_tab()
#         cls.driver = session_object.get_job('EMPLOYEMENT_STATUS')
#     def test_3(self):
#         print("*********3")
#
#     def tearDown(cls):
#         cls.driver.close()
#
#
# class Job_categories(unittest.TestCase):
#     @classmethod
#     def setUp(cls):
#         session_object = admin_tab.admin_tab()
#         cls.driver = session_object.get_job('JOB_CATEGORIES')
#     def test_4(self):
#         print("*********4")
#
#     def tearDown(cls):
#         cls.driver.close()
#
#
# class Work_shifts(unittest.TestCase):
#     @classmethod
#     def setUp(cls):
#         session_object = admin_tab.admin_tab()
#         cls.driver = session_object.get_job('WORK_SHIFTS')
#     def test_5(self):
#         print("*********5")
#
#     def tearDown(cls):
#         cls.driver.close()


if __name__ == "__main__":
    unittest.main()
