from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME, "email")
    pwdCheck = (By.ID, "exampleCheck1")
    dropDown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.XPATH, "//*[contains(@class,'alert-success')]")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPwdCheck(self):
        return self.driver.find_element(*HomePage.pwdCheck)

    def getGender(self):
        return self.driver.find_element(*HomePage.dropDown)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)