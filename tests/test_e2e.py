from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.logger import Logger


class TestOne(BaseClass):
    log = Logger().get_logger()

    def test_e2e(self):
        try:
            homepage= HomePage(self.driver)
            homepage.shopItems().click()
            checkoutpage = CheckOutPage(self.driver)
            products = checkoutpage.getproductnames()
            for product in products:
                productname = product.text
                if productname == "Blackberry":
                    checkoutpage.addmobiletocart().click()
            checkoutpage.presscheckoutbutton().click()
            checkoutpage.getcheckoutcontinousshopping().click()
            confirmpage = ConfirmPage(self.driver)
            self.log.info("Entering the country name as india")
            confirmpage.coutrysearch().send_keys("ind")
            self.verifylinkpresent("India")
            confirmpage.getcountrysearched().click()
            confirmpage.checktermsandconditioncheckbox().click()
            confirmpage.clickpurchasebutton().click()
            sucessmessage = confirmpage.getbrowsersuccessmessage().text
            self.log.info("text recived from brower" +sucessmessage)
            assert "Success!" in sucessmessage
        except Exception as e:
            self.log.error("An Exception occurred:" + str(e))
            raise Exception
