from selenium.webdriver.common.by import By


class confirmorder():
    def __init__(self, driver):
        self.driver = driver

    def confirmproduct(self):
        return self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']")

    def typeCountry(self):
        return self.driver.find_element(By.ID, "country")

    def selectCountry(self):
        return self.driver.find_element(By.LINK_TEXT, "Pakistan")

    def termsandconditions(self):
        return self.driver.find_element(By.XPATH, "//div[@class= 'checkbox checkbox-primary']")

    def purchase(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn-success")

    def successnotification(self):
        return self.driver.find_element(By.CLASS_NAME, "alert-success")


