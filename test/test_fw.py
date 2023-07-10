import time

from pageObjects.Details_page import Detailspage
from pageObjects.Home_page import Homepage
from pageObjects.Login_page import Loginpage
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class Testone(BaseClass):

    def test_e2e(self):
        lp = Loginpage(self.driver)
        lp.emailID().send_keys("rohitgaikwad9535@gmail.com")
        lp.password().send_keys("@Bigile9535")
        lp.log_in().click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Rohit Anand Gaikwad")))
        hp=Homepage(self.driver)
        hp.prof_name().click()
        time.sleep(2)
        hp.contc_info().click()
        dp=Detailspage(self.driver)
        time.sleep(2)
        print(dp.prof_link().get_attribute("href"))
        time.sleep(2)
        print(dp.ph_no().text)
        print(dp.address().get_attribute("href"))
        time.sleep(2)
        print(dp.mail_id().get_attribute("href"))
        time.sleep(2)
        print(dp.date_OB().text)


        # self.driver.find_element(By.NAME, "session_key").send_keys("rohitgaikwad9535@gmail.com")
        # time.sleep(2)
        # self.driver.find_element(By.NAME, "session_password").send_keys("@Bigile9535")
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']").click()

        # time.sleep(2)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Rohit Anand Gaikwad")))

        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "Rohit Anand Gaikwad").click()
        # time.sleep(3)
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "Contact info").click()
        # time.sleep(2)
        # print(
        #     self.driver.find_element(By.XPATH, "//a[text()='linkedin.com/in/rohit-anand-gaikwad-3bb975256']").get_attribute(
        #         "href"))
        # time.sleep(2)
        # print(self.driver.find_element(By.XPATH, "//span[text()='9490407273']").text)
        # time.sleep(2)
        # print(self.driver.find_element(By.PARTIAL_LINK_TEXT, "Rajajinagar Bangalore").get_attribute("href"))
        # time.sleep(2)
        # print(self.driver.find_element(By.PARTIAL_LINK_TEXT, "rohitgaikwad9535@gmail.com").get_attribute("href"))
        # time.sleep(2)
        # print(self.driver.find_element(By.XPATH, "//span[text()='September 15']").text)





