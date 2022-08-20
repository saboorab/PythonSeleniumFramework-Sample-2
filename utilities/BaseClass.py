import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifylinkpresent(self,text):
        waitforcountry = WebDriverWait(self.driver, 10)
        waitforcountry.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectoptionByText(self,locator,text):
        selectgender=Select(locator)
        selectgender.select_by_visible_text(text)