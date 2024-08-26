import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageobjcts.HomePage import Homepage
from pageobjcts.checkout import checkoutpage
from pageobjcts.confirmOrder import confirmorder
from utilities.BaseClass import Baseclass


class TestOne(Baseclass):

    def test_e2e(self, setup):
        driver = setup  # Get the WebDriver instance from the fixture
        log = self.getlogger()

        homepage = Homepage(driver)  # Instantiate Homepage with the WebDriver
        checkoutPage = homepage.shopitems()  # Find the shop items element
        log.info("getteing all the cards titles")

        products = checkoutPage.getcardtitels()
        for product in products:
            productName = product.find_element(By.CSS_SELECTOR, "div h4").text
            if productName == "Blackberry":
                checkoutPage.getcardfooter().click()

        confirmProduct = checkoutPage.checkoutbutton()
        confirmProduct.confirmproduct().click()
        log.info("entering country name pa")
        confirmProduct.typeCountry().send_keys("pa")
        self.verifylinks("Pakistan")
        confirmProduct.selectCountry().click()
        confirmProduct.termsandconditions().click()
        confirmProduct.purchase().click()
        successText = confirmProduct.successnotification().text
        log.info("text recieved from application is " +successText)
        assert "Success! Thank you!" in successText
