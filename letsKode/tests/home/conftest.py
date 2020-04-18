import pytest
from base.webdriver_factory import WebDriverFactory
from pages.login_page import LoginPage


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wb = WebDriverFactory(browser)
    driver = wb.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.click_login_link()
    lp.login("test@email.com", "abcabc")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    #lp.logout()
    #driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")