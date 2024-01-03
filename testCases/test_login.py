import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
        # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
        # driver = webdriver.Chrome(service=serv_obj)
        # driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        # self.driver = setup()
        self.logger.info("******************* Test_001_Login **************************")
        self.logger.info("******************* Verifying Home Page Title **************************")
        setup.get(self.baseURL)
        act_title = setup.title
        if act_title == "Your store. Login":
            assert True
            setup.close()
            self.logger.info("******************* Home Page Title Test is Passed **************************")
        else:
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "Screenshots", "test_homePageTitle.png"))#os.path.abspath(".\\Screenshots\\test_homePageTitle.png")
            print(f"Saving screenshot to: {screenshot_path}")
            setup.save_screenshot(screenshot_path)
            # setup.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            setup.close()
            self.logger.info("******************* Home Page Title is Failed **************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("******************* Verifying Login Test **************************")
        # self.driver = webdriver.Chrome()
        # self.driver = setup()
        setup.get(self.baseURL)
        self.lp = LoginPage(setup)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = setup.title
        # print(f"Actual title: {act_title}")
        # print(f"Result title: {setup.title}")
        if act_title == "Dashboard / nopcommerce administration":
            assert True
            setup.close()
            self.logger.info("******************* Login Test is Passed **************************")
        else:
            screenshot_path = os.path.abspath(os.path.join(os.getcwd(), "Screenshots", "test_login.png")) #".\\Screenshots\\test_login.png")
            print(f"Saving screenshot to: {screenshot_path}")
            setup.save_screenshot(screenshot_path)
            # setup.save_screenshot(".\\Screenshots\\" + "test_login.png")
            setup.close()
            self.logger.info("******************* Login Test is Failed **************************")
            assert False

