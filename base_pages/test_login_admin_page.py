import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginAdminPage:

    textbox_username_name="username"
    textbox_password_name="password"
    btn_login_class="orangehrm-login-button"
    logout_xpath="oxd-userdropdown-name"
    act_logout_click="//a[text()='Logout']"


    def __init__(self,driver):
        self.driver= driver

    def enter_username(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.CLASS_NAME,self.btn_login_class).click()

    def click_logout(self):
        self.driver.find_element(By.CLASS_NAME,self.logout_xpath ).click()
        self.driver.find_element(By.XPATH,self.act_logout_click ).click()

