import pytest

from pageobjcts.HomePage import Homepage
from pageobjcts.checkout import checkoutpage
from testdata.Homepagedata import Hompepagedata
from pageobjcts.confirmOrder import confirmorder
from utilities.BaseClass import Baseclass


class Testhomepage(Baseclass):

    def test_submitform(self, getdata, setup):
        driver = setup
        log = self.getlogger()

        homepage = Homepage(driver)
        log.info("User name is displayed")
        homepage.getname().send_keys(getdata["firstname"])
        log.info("User ID is displayed")
        homepage.getID().send_keys(getdata["ID"])
        homepage.getpass().send_keys('0m1k25')
        homepage.checkbox().click()
        log.info("user gender is selected")
        self.selectoption(homepage.dropDown(), getdata["gender"])
        homepage.radiobutton().click()
        homepage.submitbtn().click()
        message = homepage.successmsg().text
        log.info(message)
        assert "Success!" in message
        log.info(f"Testing with data: {getdata}")

        driver.refresh()

        checkoutpage = homepage.shopitems()
        checkoutpage.getcardtitels()
        checkoutpage.getcardfooter().click()
        confirmorder = checkoutpage.checkoutbutton()
        confirmorder.confirmproduct().click()
        confirmorder.typeCountry().send_keys("pa")
        confirmorder.selectCountry().click()
        confirmorder.termsandconditions().click()
        confirmorder.purchase().click()
        confirmorder.successnotification()
        driver.quit()





    @pytest.fixture(params=Hompepagedata.Test_Homepage_data)
    def getdata(self, request):
        return request.param



