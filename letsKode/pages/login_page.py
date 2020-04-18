import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class  LoginPage(BasePage):
    """
    Implementation of all the methods
    which will be used to test the Login Page
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login_link = "//a[@class='navbar-link fedora-navbar-link']"
    username_field = "user_email"
    password_field = "user_password"
    login_button = "commit"
    user_icon = "gravatar"
    error_message = "//div[@class='alert alert-danger']"
    logout_button = "//a[@href='/sign_out']"
    forgot_password_button = "//a[@href='/secure/42299/users/password/new']"
    forgot_password_email = "user_email"
    send_me_instruction_button = "commit"
    invalid_email_id_error_msg = "/html//form[@id='new_user']//span[@class='help-block']"
    invalid_err_msg = "We couldn't find an account with that email address"
    reset_page_title = "/html/body/div[@role='main']/div[@class='gray-layout']//h1[1]"

    def click_login_link(self):
        self.element_click(self.login_link, locator_type="xpath")

    def enter_user_name(self, username):
        self.send_key(username, self.username_field)

    def enter_password(self, password):
        self.send_key(password, self.password_field)

    def click_login_button(self):
        self.element_click(self.login_button, locator_type="name")

    def clear_username_field(self):
        self.clear_field(self.username_field)

    def clear_password_field(self):
        self.clear_field(self.password_field)

    def login(self, username="", password=""):
        self.clear_username_field()
        time.sleep(3)
        self.enter_user_name(username)
        self.clear_password_field()
        self.enter_password(password)
        self.click_login_button()
        time.sleep(3)

    def logout_link(self):
        self.element_click(self.user_icon, "class")
        time.sleep(2)
        self.element_click(self.logout_button, "xpath")

    def verify_login_successful(self):
        result = self.is_element_present(self.user_icon, locator_type="class")
        return result

    def verify_invalid_login(self):
        result = self.is_element_present(self.error_message, locator_type="xpath")
        return result

    def verify_title(self):
        return self.verify_page_title("Let's Kode It")

    def verify_forgot_password(self):
        self.element_click(self.forgot_password_button, "xpath")
        time.sleep(3)

    def enter_email_field(self, email=""):
        self.send_key(email, self.forgot_password_email)

    def click_send_me_button(self):
        self.element_click(self.send_me_instruction_button, "name")

    def verify_error_message(self):
        return self.verify_text(self.invalid_email_id_error_msg, "xpath", self.invalid_err_msg)

    def verify_reset_password_page(self):
        return self.verify_text(self.reset_page_title, "xpath", "Reset Password")




