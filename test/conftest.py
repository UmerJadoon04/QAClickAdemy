import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Name of the browser to use for tests"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name").lower()  # Normalize to lowercase

    try:
        if browser_name in ["chrome", "google chrome"]:
            service = Service(
                executable_path='C:/Users/Dell/Downloads/127.0.6533.72 chromedriver-win64/chromedriver-win64/chromedriver.exe')

            driver = webdriver.Chrome(service=service)
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name in ["microsoft edge", "edge", "msedge"]:
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            print(f"Unsupported browser '{browser_name}', defaulting to Chrome.")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://qaclickacademy.github.io/protocommerce/")
        driver.maximize_window()
        request.cls.driver = driver
        yield driver
    finally:
        if driver:
            driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


