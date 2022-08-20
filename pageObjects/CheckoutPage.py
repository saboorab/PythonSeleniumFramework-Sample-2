from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver=driver


    # mobilenames = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    addbuttoncart=(By.XPATH, "div/button")
    poductnamesall=(By.XPATH, " //div[@class='card h-100’]/div/h4/a']")
    checkoutbutton=(By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkoutcontinousshopping=(By.XPATH, "//button[@class='btn btn-success']")


    def getproductnames(self):
        return self.driver.find_elements(*CheckOutPage.poductnamesall)

    def addmobiletocart(self):
        return self.driver.find_element(*CheckOutPage.addbuttoncart)

    def presscheckoutbutton(self):
        return self.driver.find_element(*CheckOutPage.checkoutbutton)

    def getcheckoutcontinousshopping(self):
        return self.driver.find_element(*CheckOutPage.checkoutcontinousshopping)
