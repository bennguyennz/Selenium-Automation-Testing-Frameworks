import pytest
from Driver.webdriver_factory import GetWebdriverInstance

# Send request variable to the fixture
## Browser value will be set from request.config.getoption (from command prompt)
@pytest.yield_fixture(scope="class")
def invoke_browser(request,browser):
    wdf = GetWebdriverInstance(browser)
    driver = wdf.getbrowserInstance()

    # Set class attribute and assign the variable
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

# Create 2 parsers to get value from command prompt
def pytest_addoption(parser):
    parser.addoption("--browser")

#Return the argument value
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
