import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import Base_class


class TestHomePage(Base_class):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        #homePage.getName().send_keys(getData[0])
        log.info("first name is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        #driver.find_element_by_css_selector("input[name='name']").send_keys("Suchithra")
        #driver.find_element_by_name("email").send_keys("abc@gmail.com")
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPwdCheck().click()
        #driver.find_element_by_id("exampleCheck1").click()

        self.selectOptionByText(homePage.getGender(),getData["gender"])

        homePage.getSubmit().click()
        #driver.find_element_by_xpath("//input[@type='submit']").click()

        # txt = driver.find_element_by_css_selector("[class*='alert-success']").text

        # txt = driver.find_element_by_class_name("alert-success").text
        #txt = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
        txt = homePage.getSuccess().text

        print(txt)

        assert "Success!" in txt
        self.driver.refresh()

    # @pytest.fixture(params=[("Suchi","abc@gmail.com","Female"),("sarva","134@gmail.com", "Male")])
    # def getData(self, request):
    #     return request.param

    @pytest.fixture(params = HomePageData.getTestData("testcase2"))
    def getData(self, request):
         return request.param
