import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util


class RegisterCourseClass(BasePage):
    """
    Implementation of the methods which is used to test the course
    registration and end to end scenarios
    """

    log = cl.customLogger(logging.DEBUG)
    ut = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_box = "search-courses"
    search_button = "search-course-button"
    course_list = "course-listing-title"
    enroll_button = "enroll-button-top"
    card_number = "cardnumber"
    expiration_date = "exp-date"
    cvv_number = "cvc"
    postal_code = "postal"
    terms_condition_button = "agreed_to_terms_checkbox"
    submit_button = "confirm-purchase"
    error_message = "//div[@class='payment-error-box only-on-mobile']//span[contains(text(),'The card was declined.')]"
    confirm_button = "//button[@id ='confirm-purchase']"
    home_page_button = "//a[@class='navbar-brand header-logo']"
    category_dropdown = "/html/body/div[@role='main']//div[@class='row search']/div[1]/div[@class='btn-group']/button[@type='button']/span[@class='caret']"
    all_link = "All"
    software_test_link = "Software Testing (6)"
    software_dev_link = "Software Development (8)"
    software_it_link = "Software IT (4)"
    react_hooks = "React Hooks (1)"
    heading_software_testing_page = "//div[@role='main']//h2[text()='Software Testing']"
    selenium_webdriver_with_java = "//div[@title='Selenium WebDriver With Java']"
    selenium_webdriver_bundle = "//div[@title='Selenium WebDriver Bundle (Java + Python)']"
    complete_test_automation_bundle = "//div[@title='Complete Test Automation Bundle']"
    testng_complete_bootcamp = "//div[@title='TestNG Complete Bootcamp - Novice To Ninja']"
    rest_api_automation = "//div[@title='Rest API Automation With Rest Assured']"
    selenium_webdriver_advanced = "//div[@title='Selenium WebDriver Advanced']"


    def enterCourseName(self, course_name):
        self.element_click(self.search_box)
        self.send_key(course_name, self.search_box)

    def clickSearchButton(self):
        self.element_click(self.search_button)

    def selectCourseToEnroll(self):
        self.element_click(self.course_list, locator_type="class")

    def clickEnrollButton(self):
        self.element_click(self.enroll_button)

    def scrolldown(self):
        self.web_scroll(direction="down")

    def scrollup(self):
        self.web_scroll(direction="up")

    def enterCardNum(self, card_number):
        self.switch_to_frame(index=2)
        self.send_key(card_number, self.card_number, locator_type="name")
        self.switch_to_default()

    def enterExpDate(self, exp_date):
        self.switch_to_frame(index=3)
        self.send_key(exp_date, self.expiration_date, locator_type="name")
        self.switch_to_default()

    def enterCvvNum(self, cvv_number):
        self.switch_to_frame(index=4)
        self.send_key(cvv_number, self.cvv_number, locator_type="name")
        self.switch_to_default()

    def enterPostalCode(self, postal_code):
        self.switch_to_frame(index=5)
        self.send_key(postal_code, self.postal_code, locator_type="name")
        self.switch_to_default()

    def clickTermsButton(self):
        self.element_click(self.terms_condition_button)

    def enrollButton(self):
        self.is_element_displayed(self.submit_button)

    def confirmButton(self):
        self.element_click(self.confirm_button, "xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterExpDate(exp)
        self.enterCvvNum(cvv)

    def enrollCourse(self, num="", exp="", cvv="", zipcode=""):
        self.clickEnrollButton()
        self.ut.sleep(3, "After clicking login icon")
        self.scrolldown()
        self.enterCreditCardInformation(num, exp, cvv)
        self.enterPostalCode(zipcode)
        self.clickTermsButton()
        self.confirmButton()
        self.ut.sleep(20)

    def verifyErrorMessage(self):
        result = self.verify_text(self.error_message, "xpath", "The card was declined.")
        return result

    def clickHomePageButton(self):
        self.element_click(self.home_page_button, "xpath")

    def select_category_dropdown(self):
        self.element_click(self.category_dropdown, "xpath")

    def click_all_menu_link(self):
        self.element_click(self.all_link, "link")

    def click_software_testing_link(self):
        self.element_click(self.software_test_link, "link")
        result = self.is_element_present(self.heading_software_testing_page, "xpath")
        return result

    def verify_selenium_webdriver_with_java(self, course_1):
        result = self.verify_text(self.selenium_webdriver_with_java, "xpath", course_1)
        return result

    def verify_selenium_webDriver_bundle(self, course_2):
        result = self.verify_text(self.selenium_webdriver_bundle, "xpath", course_2)
        return result

    def verify_complete_test_automation_bundle(self, course_3):
        result = self.verify_text(self.complete_test_automation_bundle, "xpath", course_3)
        return result

    def verify_testNG_complete_bootcamp(self, course_4):
        result = self.verify_text(self.testng_complete_bootcamp, "xpath", course_4)
        return result

    def verify_rest_api_automation(self, course_5):
        result = self.verify_text(self.rest_api_automation, "xpath", course_5)
        return result

    def verify_selenium_webDriver_advanced(self, course_6):
        result = self.verify_text(self.selenium_webdriver_advanced, "xpath", course_6)
        return result

    def click_software_dev_link(self):
        self.element_click(self.software_dev_link, "link")

    def click_software_it_link(self):
        self.element_click(self.software_it_link, "link")

    def click_react_hooks_link(self):
        self.element_click(self.react_hooks, "link")






















