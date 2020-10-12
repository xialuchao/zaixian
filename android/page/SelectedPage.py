from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from android.driver.Client import AndroidClient
from android.page.BasePage import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def gotoHS(self):
        self.findByText("沪深").click()
        return self
    def getPriceByName(self, name) -> float:
        priceLocator=(MobileBy.XPATH, "//*[contains(@resource-id, 'stockName') and @text='%s']" %name +
             "/../../..//*[contains(@resource-id, 'currentPrice')]")
        price=self.find(priceLocator).text
        return float(price)