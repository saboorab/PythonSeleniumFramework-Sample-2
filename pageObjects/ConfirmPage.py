from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver=driver

    searchcountryname=(By.ID, "country")
    countrylocated=(By.LINK_TEXT, "India")
    termsandconditioncheckbox=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchasebutton=(By.CSS_SELECTOR, "input[type='submit']")
    Successmessagebrowser=(By.CLASS_NAME, "alert-success")


    def coutrysearch(self):
        return self.driver.find_element(*ConfirmPage.searchcountryname)

    def getcountrysearched(self):
        return self.driver.find_element(*ConfirmPage.countrylocated)

    def checktermsandconditioncheckbox(self):
        return self.driver.find_element(*ConfirmPage.termsandconditioncheckbox)

    def clickpurchasebutton(self):
        return self.driver.find_element(*ConfirmPage.purchasebutton)

    def getbrowsersuccessmessage(self):
        return self.driver.find_element(*ConfirmPage.Successmessagebrowser)