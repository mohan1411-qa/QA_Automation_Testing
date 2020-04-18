import unittest
from tests.home.login_tests import LoginTests
from tests.home.register_courses_tests import RegisterCourseTest
from tests.home.sign_up_tests import SignUpTest

""" Import all the test cases from test classes """
tc_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseTest)
tc_3 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)

"Create the test suite based on the requirement"
smoke_test = unittest.TestSuite([tc_1, tc_2, tc_3])
unittest.TextTestRunner(verbosity=2).run(smoke_test)
