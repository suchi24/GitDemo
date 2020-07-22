from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    #"button[class*='btn-success']"
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    chkBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    btnCheckout = (By.CSS_SELECTOR,"button[class*='btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getchkBtn(self):
        return self.driver.find_element(*CheckoutPage.chkBtn)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def CheckoutItems(self):
        self.driver.find_element(*CheckoutPage.btnCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage