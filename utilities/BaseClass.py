import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class Baseclass:
    driver = None  # Explicitly declare the driver attribute to avoid IDE warnings

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s %(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifylinks(self, text):
        # Use self.driver directly since it's already assigned by the fixture
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
        return element

    def selectoption(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)


