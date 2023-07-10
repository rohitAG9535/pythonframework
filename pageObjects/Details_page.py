from selenium.webdriver.common.by import By


class Detailspage:

    def __init__(self, driver):
        self.driver = driver


    link = (By.XPATH, "//a[text()='linkedin.com/in/rohit-anand-gaikwad-3bb975256']")
    phno = (By.XPATH, "//span[text()='9490407273']")
    adr = (By.PARTIAL_LINK_TEXT, "Rajajinagar Bangalore")
    mail = (By.PARTIAL_LINK_TEXT, "rohitgaikwad9535@gmail.com")
    dob = (By.XPATH, "//span[text()='September 15']")


    def prof_link(self):
        return self.driver.find_element(*Detailspage.link)

    def ph_no(self):
        return self.driver.find_element(*Detailspage.phno)

    def address(self):
        return self.driver.find_element(*Detailspage.adr)

    def mail_id(self):
        return self.driver.find_element(*Detailspage.mail)

    def date_OB(self):
        return self.driver.find_element(*Detailspage.dob)


