from pages.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVDATA
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        result_1 = self.lp.verify_title()
        self.ts.mark(result_1, "Test Verified")
        self.lp.login("test@email.com", "abcabc")
        result_2 = self.lp.verify_login_successful()
        self.ts.markFinal("Valid Login", result_2, "Test Failed")

    @pytest.mark.run(order=1)
    @data(*getCSVDATA("F:/Project_Workspace/letsKode/test_data/login_page_test_data.csv"))
    @unpack
    def test_invalid_login(self, username, password):
        self.lp.logout_link()
        self.lp.click_login_link()
        self.lp.login(username, password)
        result = self.lp.verify_invalid_login()
        self.ts.markFinal("Invalid Login", result, "Test Failed")

    @pytest.mark.run(order=3)
    @data(*getCSVDATA("F:/Project_Workspace/letsKode/test_data/forgot_password_test_data.csv"))
    @unpack
    def test_forgot_password(self, email):
        self.lp.logout_link()
        self.lp.click_login_link()
        time.sleep(3)
        self.lp.verify_forgot_password()
        time.sleep(2)
        result_1 = self.lp.verify_reset_password_page()
        self.ts.mark(result_1, "Test Failed")
        self.lp.enter_email_field(email)
        self.lp.click_send_me_button()
        result_2 = self.lp.verify_error_message()
        self.ts.markFinal("Invalid email id verification", result_2, "Test Failed")



