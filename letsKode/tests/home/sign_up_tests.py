import unittest
import pytest
from pages.sign_up_page import SignUpPage
from utilities.test_status import TestStatus
from ddt import ddt, data, unpack
from pages.login_page import LoginPage
from utilities.read_data import getCSVDATA


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class SignUpTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.sp = SignUpPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVDATA("F:/Project_Workspace/letsKode/test_data/sign_up_page_test_data.csv"))
    @unpack
    def test_sign_up_button_validation(self, username,email,password,confirm_password):
        self.lp.logout_link()
        self.sp.click_signup_link()
        result_1 = self.sp.verify_page_title()
        self.ts.mark(result_1, "Page Verification Successful")
        self.sp.enter_sign_up_information(username, email, password, confirm_password)
        self.sp.click_condition_checkbox()
        self.sp.click_terms_condition_checkbox()
        result_2 = self.sp.click_signup_button()
        self.ts.markFinal("sign_up_button_validation", result_2, "Test Successful")

    @pytest.mark.run(order=2)
    @data(*getCSVDATA("F:/Project_Workspace/letsKode/test_data/sign_up_page_test_data.csv"))
    @unpack
    def test_captcha_element(self, username, email, password, confirm_password):
        self.sp.click_home_button_link()
        self.sp.click_enroll_now_button()
        result_1 = self.sp.verify_page_title()
        self.ts.mark(result_1, "Enroll button and Page Verification Successful")
        self.sp.enter_sign_up_information(username, email, password, confirm_password)
        result_2 = self.sp.check_captch_checkbox()
        self.ts.markFinal("Verfication of presence of captcha element", result_2, "Test Successful")











