from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """
    This is the locator class for the login page where the login page locators are defined
    """
    EMAIL_ID = (By.XPATH, '//*[@id="txtUsername"]')
    PASSWORD = (By.XPATH, '//*[@id="txtPassword"]')
    LOGIN = (By.XPATH, '//*[@id="btnLogin"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="spanMessage"]')
    LOGOUT = (By.XPATH, '//*[@id="welcome-menu"]/ul/li[2]/a')

class Admin(object):

        CLICK_ADMIN = (By.XPATH, '//*[@id="menu_admin_viewAdminModule"]/b')
        USERS = (By.XPATH, '//*[@id="menu_admin_viewSystemUsers"]')
        ADD_BUTTON = (By.XPATH, '//*[@id="btnAdd"]')

class UserManagement(object):
    USER_ROLE = (By.NAME, 'systemUser[userType]')
    EMPLOYEE_NAME = (By.XPATH, '//*[@id="systemUser_employeeName_empName"]')
    USERNAME = (By.XPATH, '//*[@id="systemUser_userName"]')
    STATUS = (By.ID, 'systemUser_status')
    PASSWORD = (By.XPATH, '//*[@id="systemUser_password"]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="systemUser_confirmPassword"]')
    EMPLOYEE_NAME_DROPDOWN = (By.XPATH, '/html/body/div[4]/ul/li[2]')
    SAVE_USER_BUTTON = (By.XPATH, '//*[@id="btnSave"]')
    CANCEL_USER_BUTTON = (By.XPATH, '//*[@id="btnCancel"]')
    DELETE_USER_BUTTON = (By.XPATH,'//*[@id="btnDelete"]')
    CONFIRM_DELETE_USER_BUTTON = (By.XPATH,'//*[@id="dialogDeleteBtn"]')
    TABLE_ID= (By.ID, 'resultTable')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="searchBtn"]')
    SEARCH_USERNAME = (By.XPATH, '//*[@id="searchSystemUser_userName"]')
    SEARCH_USER_ROLE = (By.XPATH, '//*[@id="searchSystemUser_userType"]')
    SEARCH_EMPLOYEE_NAME = (By.XPATH, '//*[@id="searchSystemUser_employeeName_empName"]')
    SEARCH_EMPLOYEE_NAME_LIST = (By.XPATH, '/html/body/div[4]/ul/li[3]')
    SEARCH_STATUS = (By.XPATH, '//*[@id="searchSystemUser_status"]')
    RESET_SEARCH = (By.XPATH, '//*[@id="resetBtn"]')

class Job(object):
    JOB_TAB = (By.XPATH, '//*[@id="menu_admin_Job"]')
    JOB_TITTLE = (By.XPATH, '//*[@id="menu_admin_viewJobTitleList"]')
    JOB_TITTLE_ADD = (By.XPATH, '//*[@id="btnAdd"]')
    JOB_TITTLE_MESSAGE = (By.XPATH, '//*[@id="frmSavejobTitle"]/fieldset/ol/li[1]/span')
    JOB_TITTLE_DELETE = (By.XPATH, '//*[@id="btnDelete"]')
    JOB_TITTLE_CANCEL = (By.XPATH, '//*[@id="btnCancel"]')
    JOB_TITTLE_DELETE_CONFIRMATION = (By.XPATH, '//*[@id="dialogDeleteBtn"]')
    JOB_TITTLE_TABLE = (By.ID, 'resultTable')
    ADD_JOB_TITTLE = (By.XPATH, '//*[@id="jobTitle_jobTitle"]')
    JOB_DESCRIPTION = (By.XPATH, '//*[@id="jobTitle_jobDescription"]')
    JOB_SPECIFICATION = (By.XPATH, '//*[@id="jobTitle_jobSpec"]')
    NOTE = (By.XPATH, '//*[@id="jobTitle_note"]')
    SAVE_JOB_TITTLE = (By.XPATH, '//*[@id="btnSave"]')
    CANCEL_JOB_TITTLE = (By.XPATH, '//*[@id="btnCancel"]')

    PAY_GRADES = (By.XPATH, '//*[@id="menu_admin_viewPayGrades"]')
    PAY_GRADES_ADD_BUTTON = (By.XPATH, '//*[@id="btnAdd"]')
    PAY_GRADES_DELETE_BUTTON = (By.XPATH, '//*[@id="btnDelete"]')
    PAY_GRADES_TABLE = (By.XPATH, '//*[@id="resultTable"]')
    PAY_GRADE_ADD_NAME = (By.XPATH, '//*[@id="payGrade_name"]')
    PAY_GRADES_NAME_MESSAGE = (By.XPATH, '//*[@id="frmPayGrade"]/fieldset/ol/li[1]/span')
    PAY_GRADES_SAVE = (By.XPATH, '//*[@id="btnSave"]')
    PAY_GRADES_CANCEL = (By.XPATH, '//*[@id="btnCancel"]')
    ADD_CURRENCY = (By.XPATH, '//*[@id="btnAddCurrency"]')
    CURRENCY_TABLE = (By.XPATH, '//*[@id="tblCurrencies"]')
    CURRENCY_NAME = (By.XPATH, '//*[@id="payGradeCurrency_currencyName"]')
    MINIMUM_SALARY = (By.XPATH, '//*[@id="payGradeCurrency_minSalary"]')
    MAXIMUM_SALARY = (By.XPATH, '//*[@id="payGradeCurrency_maxSalary"]')
    SAVE_CURRENCY_BUTTON = (By.XPATH, '//*[@id="btnSaveCurrency"]')
    CANCEL_CURRENCY_BUTTON = (By.XPATH, '//*[@id="cancelButton"]')

    EMPLOYEMENT_STATUS = (By.XPATH, '//*[@id="menu_admin_employmentStatus"]')
    JOB_CATEGORIES = (By.XPATH, '//*[@id="menu_admin_jobCategory"]')
    WORK_SHIFTS = (By.XPATH, '//*[@id="menu_admin_workShift"]')







