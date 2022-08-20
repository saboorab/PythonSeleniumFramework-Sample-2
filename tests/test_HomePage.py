import time

import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.logger import Logger


class TestHomePage(BaseClass):
    log = Logger().get_logger()

    def test_formsubmission(self,getData):
        try:
            homepage=HomePage(self.driver)
            self.log.info("firstname is " + getData["firstname"])
            homepage.getname().send_keys(getData["firstname"])
            homepage.getemail().send_keys(getData["lastname"])
            homepage.checkLoveicecreamCheckbox().click()
            self.selectoptionByText(homepage.getgender(), getData["gender"])
            homepage.Presssubmitform().click()
            successalert=homepage.getSuccessalert().text
            self.log.info("get the message from browser" + successalert )
            assert "Success!" in successalert
            self.driver.refresh()
        except Exception as e:
            self.log.error("An Exception occurred:" + str(e))
            raise Exception(e)

    @pytest.fixture(params=HomePageData.gettestData("Testcase2"))
    def getData(self,request):
        return request.param
