from base.basepage import BasePage
import time
import utilities.custom_logger as cl
import logging


class SignUpPage(BasePage):
    """
    Implementation of all the methods
    which will be used to test the SignUp Page
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    sign_up_link = "header-sign-up-btn"
    name_field = "user_name"
    email_field = "user_email"
    password_field = "user_password"
    confirm_password_field = "user_password_confirmation"
    captcha_field = "rc-anchor-container"
    condition_checkbox = "user_unsubscribe_from_marketing_emails"
    terms_condition_checkbox = "user_agreed_to_terms"
    sign_up_button = "//input[@disabled='disabled']"
    home_button_link = "//a[@class='navbar-brand header-logo']"
    captcha_image = "rc-imageselect"
    sign_up_page_title = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]"
    page_title = "Sign Up to Let's Kode It"
    enroll_now_button = "/html//div[@role='main']/div/div[1]//a[@href='/sign_up']"

    def click_signup_link(self):
        self.element_click(self.sign_up_link)

    def enter_name(self, data):
        self.send_key(data, self.name_field)

    def enter_email(self, data):
        self.send_key(data, self.email_field)

    def enter_password(self, data):
        self.send_key(data, self.password_field)

    def enter_confirm_password(self, data):
        self.send_key(data, self.confirm_password_field)

    def click_condition_checkbox(self):
        self.element_click(self.condition_checkbox)

    def click_terms_condition_checkbox(self):
        self.element_click(self.terms_condition_checkbox)

    def click_signup_button(self):
        exp_result = self.is_element_enabled(self.sign_up_button, "xpath")
        result = self.modify_result(expected_result=False, actual_result=exp_result)
        return result

    def enter_sign_up_information(self, name, email, password, confirm_password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)

    def click_home_button_link(self):
        self.web_scroll("up")
        self.element_click(self.home_button_link, "xpath")

    def check_captch_checkbox(self):
        self.web_scroll("down")
        self.switch_to_frame(id=2)
        result = self.is_element_enabled(self.captcha_field)
        self.element_click(self.captcha_field)
        self.switch_to_default()
        return result

    def verify_page_title(self):
        result = self.verify_text(self.sign_up_page_title, "xpath", self.page_title)
        time.sleep(2)
        return result

    def click_enroll_now_button(self):
        self.element_click(self.enroll_now_button, "xpath")

