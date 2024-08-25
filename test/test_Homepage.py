import pytest

from pageobjcts.HomePage import Homepage
from testdata.Homepagedata import Hompepagedata
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
        self.driver.refresh()

    @pytest.fixture(params=Hompepagedata.Test_Homepage_data)
    def getdata(self, request):
        return request.param



