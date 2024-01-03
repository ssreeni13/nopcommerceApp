import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.Addcustomerpage import AddCustomer
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("******************* Test_003_DDT_AddCustomer **************************")
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************* Login Successful **************************")

        self.logger.info("******************* Starting Add Customer Test **************************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("********* Providing Customer Info ************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sreenivasan")
        self.addcust.setLastName("A")
        self.addcust.setDob("13/02/1997") #Format: DD / MM / YY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for Testing........")
        self.addcust.clickOnSave()

        self.logger.info("*************** Saving Customer Info *****************")

        self.logger.info("*************** Add Customer Validation Started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'customer has been added succesfully.' in self.msg:
            assert True == True
            self.logger.info("*************** Add Customer Test Passed *****************")
        else:
            self.driver.save_screenshot(".\\SCreenshots\\" + "test_addCustomer_scr.png")
            self.logger.info("*************** Add Customer Test Failed *****************")
            assert True == False

        self.driver.close()
        self.logger.info("*************** Ending Homepage Title Test *****************")


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
