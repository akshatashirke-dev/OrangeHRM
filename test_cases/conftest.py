from pygments.lexer import default
from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="Specify the browser:chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):

    global driver

    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='Firefox':
        driver=webdriver.Firefox()
    elif browser=='Edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("unsupported browser")
    return driver
#
# def pytest_configure(config):
#     config._metadata = {}

def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'OrangeHRM'
    config.stash[metadata_key]['Module Name'] = 'Admin Login'
    config.stash[metadata_key]['Tester'] = 'Akshata'
    config.stash[metadata_key]['Environment'] = 'QA'
    config.stash[metadata_key]['Browser'] = config.getoption("--browser")

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
    metadata.pop("Platform", None)
