
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.test_login_admin_page import LoginAdminPage
from utilities.read_properties import config, ReadConfig
from utilities.custome_logger import log_maker
from utilities import excel_utils

class Test02AdminLoginDataDriven:
    admin_url= ReadConfig.get_page_url()
    path='.//test_data//Admin_login_data.xlsx'
    status_list=[]
    logger = log_maker.log_gen()
    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_url)
        self.driver.implicitly_wait(10)
        self.admin_lp=LoginAdminPage(self.driver)
        self.rows =excel_utils.get_row_count(self.path,'Sheet1')
        print("rows count is:" ,self.rows)


        for r in range(2, self.rows+1):
            self.username=excel_utils.read_data(self.path,'Sheet1',r,2)
            self.password=excel_utils.read_data(self.path, 'Sheet1', r, 3)
            self.exp_login = excel_utils.read_data(self.path, 'Sheet1', r, 4)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.login_button()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = 'OrangeHRM'
            # self.admin_lp.click_logout()

            if act_title==exp_title:
                if self.exp_login=='Yes':
                    self.logger.info('login passed')
                    self.logger.info('**********valid_login_data_Driven************')
                    self.status_list.append('pass')
                    # self.admin_lp.click_logout()
                elif self.exp_login=='No':
                    self.logger.info('login failed')
                    self.status_list.append('fail')
            if act_title!=exp_title:
                if self.exp_login=='Yes':
                    self.logger.info('login failed')
                    self.status_list.append('fail')

                elif self.exp_login=='No':
                    self.logger.info('login passed')
                    self.status_list.append('pass')

        print("status list as:",self.status_list)

        if 'fail' in self.status_list:
            self.logger.info("test data driven test failed")
            assert False
        else:
            self.logger.info("test data driven test passed")
            assert True
            self.driver.close()

