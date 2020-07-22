from selenium.webdriver.common.by import By
class ConfirmPage:

    #self.driver.find_element_by_xpath("//*[contains(@class,'checkbox-primary')]").click()
    #self.driver.find_element_by_id("country").send_keys("ind")
    #self.driver.find_element_by_link_text("India").click()
    country_txtbox = (By.ID, "country")
    select_country = (By.LINK_TEXT, "India")
    chkBox_confirm = (By.XPATH, "//*[contains(@class,'checkbox-primary')]")
    purchase_btn = (By.CSS_SELECTOR, "[type='submit']")
    success_msg = (By.XPATH, "//div[contains(@class,'alert-success')]")

    def __init__(self, driver):
        self.driver = driver

    def getText(self):
        return self.driver.find_element(*ConfirmPage.country_txtbox)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.select_country)

    def chkBoxAgree(self):
        return self.driver.find_element(*ConfirmPage.chkBox_confirm)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def message(self):
        return self.driver.find_element(*ConfirmPage.success_msg)