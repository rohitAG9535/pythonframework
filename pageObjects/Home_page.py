from selenium.webdriver.common.by import By



class Homepage:

    def __init__(self, driver):
        self.driver = driver

    prof = (By.PARTIAL_LINK_TEXT, "Rohit Anand Gaikwad")
    contact = (By.PARTIAL_LINK_TEXT, "Contact info")

    def prof_name(self):
        return self.driver.find_element(*Homepage.prof)

    def contc_info(self):
        return  self.driver.find_element(*Homepage.contact)


