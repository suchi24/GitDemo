import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import Base_class


class TestOne(Base_class):
    def test_e2eTest(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        #self.driver.find_element_by_css_selector("a[href*='shop']").click()

        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        checkOutPage = homePage.shopItems()
        cards = checkOutPage.getCardTitles()

        #chkout = self.driver.find_element_by_css_selector("a[class*='btn-primary']").text
        chkout = checkOutPage.getchkBtn().text
        words = chkout.split(" ")
        count1 = int(words[2])
        log.info("count1 = " + str(count1))
        i = -1

        for card in cards:
            #blkBerr = product.find_element_by_xpath("div/h4/a")
            i = i + 1
            cardText = card.text
            log.info("card Text " + cardText)
            if (cardText) == "Blackberry":
                #product.find_element_by_xpath("div/button").click()
                checkOutPage.getcardFooter()[i].click()
                #chkout = self.driver.find_element_by_css_selector("a[class*='btn-primary']").text
                chkout = checkOutPage.getchkBtn().text
                words = chkout.split(" ")
                count2 = int(words[2])
                log.info("count2 = " + str(count2))

                assert (count1+1) == count2
                #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
                checkOutPage.getchkBtn().click()

        #self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
      #self.driver.find_element_by_xpath("//*[contains(@class,'checkbox-primary')]").click()
        confirmPage = checkOutPage.CheckoutItems()
        log.info("entering country info")
        confirmPage.getText().send_keys("ind")
        # self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresence("India")

        confirmPage.getCountry().click()
        confirmPage.chkBoxAgree().click()

        #self.driver.find_element_by_css_selector("[type='submit']").click()
        confirmPage.purchase().click()

        # assert driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text == "Success! Thank you! Your order will be delivered in next few weeks :-)."

        #successText = self.driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text
        successText = confirmPage.message().text
        log.info("Text received "+ successText )
        assert "Success! Thank you!" in successText