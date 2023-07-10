from selenium.webdriver.common.by import By


class Loginpage:


    def __init__(self, driver):
        self.driver = driver


    email = (By.NAME, "session_key")
    pwd = (By.NAME, "session_password")
    submit = (By.XPATH,"//button[@data-id='sign-in-form__submit-btn']")


    def emailID(self):
        return self.driver.find_element(*Loginpage.email)

    def password(self):
        return self.driver.find_element(*Loginpage.pwd)

    def log_in(self):
        return self.driver.find_element(*Loginpage.submit)