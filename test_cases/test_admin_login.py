import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.test_login_admin_page import LoginAdminPage
from utilities.read_properties import config, ReadConfig
from utilities.custome_logger import log_maker

class Test01AdminLogin:
    admin_url= ReadConfig.get_page_url()
    admin_username= ReadConfig.get_username()
    admin_password= ReadConfig.get_password()
    invalid_username= ReadConfig.get_invalid_username()
    logger=log_maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info('**********test_title_verification*************')
        self.driver= setup
        self.driver.get(self.admin_url)
        act_title= self.driver.title
        if act_title=='OrangeHRM':
            self.logger.info('**********title_matched*************')
            assert True
            self.driver.close()
        else:
            self.logger.info('**********title_unmatched*************')
            self.driver.close()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):

        self.driver = setup
        self.driver.get(self.admin_url)
        self.driver.implicitly_wait(10)
        self.admin_lp=LoginAdminPage(self.driver)
        self.admin_lp.enter_username(self.admin_username)
        self.admin_lp.enter_password(self.admin_password)
        self.admin_lp.login_button()
        act_title = self.driver.title
        if act_title == 'OrangeHRM':
            self.logger.info('**********valid_login************')
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_url)
        self.driver.implicitly_wait(10)
        self.admin_lp = LoginAdminPage(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.admin_password)
        self.admin_lp.login_button()
        error_msg=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p').text
        if error_msg== 'Invalid credentials':
            self.logger.info('**********Invalid_login************')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\screenshots\\test_invalid_admin_login.png')
            self.driver.close()
            assert False





