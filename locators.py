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
    STATUS = (By.XPATH, '')
    PASSWORD = (By.XPATH, '//*[@id="systemUser_password"]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="systemUser_confirmPassword"]')
    SAVE_USER_BUTTON = (By.XPATH, '//*[@id="btnSave"]')
    CANCEL_USER_BUTTON = (By.XPATH, '//*[@id="btnCancel"]')
    TABLE_ID= (By.ID, 'resultTable')




