from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        ops = webdriver.ChromeOptions()
        ops.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
        # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
        # driver = webdriver.Chrome(service=serv_obj)
        ops.add_argument("--enable-chrome-browser-cloud-management")
        driver = webdriver.Chrome(options=ops)
        print("Launching Chrome Browser.............")
        # driver = webdriver.Chrome()
        # return driver
        yield driver
        driver.quit()
    elif browser == 'firefox':
        ops = webdriver.FirefoxOptions()
        ops.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
        # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
        # driver = webdriver.Chrome(service=serv_obj)
        ops.add_argument("--enable-chrome-browser-cloud-management")
        driver = webdriver.Firefox(options=ops)
        print("Launching Firefox Browser.............")
        # driver = webdriver.Chrome()
        # return driver
        yield driver
        driver.quit()
    else:
        driver = webdriver.Ie()
    yield driver
    driver.quit()


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

################################### PyTest HTML Report #########################################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sreenivasan'

# It is hook for delete/Modify Environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)