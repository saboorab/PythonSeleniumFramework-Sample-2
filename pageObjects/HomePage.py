from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver=driver


    shop= (By.CSS_SELECTOR,"a[href*='shop']")
    name=(By.NAME, "name")
    email=(By.NAME, "email")
    LoveicecreamCheckbox=(By.ID, "exampleCheck1")
    gender=(By.ID, "exampleFormControlSelect1")
    submitform=(By.XPATH, "//input[@value='Submit']")
    Successalert=(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")







    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def checkLoveicecreamCheckbox(self):
        return self.driver.find_element(*HomePage.LoveicecreamCheckbox)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def Presssubmitform(self):
        return self.driver.find_element(*HomePage.submitform)

    def getSuccessalert(self):
        return self.driver.find_element(*HomePage.Successalert)
