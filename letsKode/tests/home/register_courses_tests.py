import unittest
import pytest
from pages.courses.register_courses_page import RegisterCourseClass
from utilities.test_status import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVDATA
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class RegisterCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.courses = RegisterCourseClass(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=6)
    @data(*getCSVDATA("F:/Project_Workspace/letsKode/test_data/register_course_test_data.csv"))
    @unpack
    def test_validEnrollment(self, course_name, card_number, exp_date, cvv_num, pin_code):
        self.courses.enterCourseName(course_name)
        self.courses.clickSearchButton()
        self.courses.selectCourseToEnroll()
        self.courses.enrollCourse(card_number, exp_date, cvv_num, pin_code)
        result = self.courses.verifyErrorMessage()
        self.ts.markFinal("Enroll Course", result, "Test Executed Successful")
        self.courses.scrollup()
        self.courses.clickHomePageButton()

    @pytest.mark.run(order=1)
    def test_category_dropdown(self):
        self.courses.select_category_dropdown()
        self.courses.click_all_menu_link()

    @pytest.mark.run(order=1)
    @data(*getCSVDATA("F:/Project_Workspace/letsKode/test_data/software_testing_course_data.csv"))
    @unpack
    def test_software_testing_link(self,course_1, course_2, course_3, course_4, course_5, course_6):
        self.courses.select_category_dropdown()
        time.sleep(2)
        res_1 = self.courses.click_software_testing_link()
        self.ts.mark(res_1, "Test Successful")
        time.sleep(2)
        res_2 = self.courses.verify_selenium_webdriver_with_java(course_1)
        self.ts.mark(res_2, "Verified course - 1")
        time.sleep(2)
        res_3 = self.courses.verify_selenium_webDriver_bundle(course_2)
        self.ts.mark(res_3, "Verified course - 2")
        time.sleep(2)
        res_4 = self.courses.verify_complete_test_automation_bundle(course_3)
        self.ts.mark(res_4, "Verified course - 3")
        time.sleep(2)
        res_5 = self.courses.verify_testNG_complete_bootcamp(course_4)
        self.ts.mark(res_5, "Verified course - 4")
        time.sleep(2)
        res_6 = self.courses.verify_rest_api_automation(course_5)
        self.ts.mark(res_6, "Verified course - 5")
        time.sleep(2)
        res_7 = self.courses.verify_selenium_webDriver_advanced(course_6)
        self.ts.markFinal("Testing Course Verified", res_7, "Verified course - 6")
        time.sleep(2)

    @pytest.mark.run(order=3)
    def test_software_dev_link(self):
        self.courses.select_category_dropdown()
        self.courses.click_software_dev_link()

    @pytest.mark.run(order=4)
    def test_software_it_link(self):
        self.courses.select_category_dropdown()
        self.courses.click_software_it_link()

    @pytest.mark.run(order=5)
    def test_react_hooks(self):
        self.courses.select_category_dropdown()
        self.courses.click_react_hooks_link()




