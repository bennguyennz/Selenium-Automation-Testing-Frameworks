import pytest
from Pages.home.login_page import LoginPage
from Base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    #print("Running method level setUp")
    yield
    #print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    #print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("nguyenbinhit@gmail.com", "1234576")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    #print("Running one time tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUpNoLogin(request, browser):
    #print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    #lp = LoginPage(driver)
    #lp.login("nguyenbinhit@gmail.com", "1234576")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    #print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")