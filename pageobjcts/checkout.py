from selenium.webdriver.common.by import By

from pageobjcts.confirmOrder import confirmorder


class checkoutpage():
    def __init__(self, driver):
        self.driver = driver


    def getcardtitels(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")

    def getcardfooter(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".card-footer button")

    def checkoutbutton(self):
        self.driver.find_element(By.XPATH, "//li/a[@class = 'nav-link btn btn-primary']").click()
        confirmProduct = confirmorder(self.driver)
        return confirmProduct



