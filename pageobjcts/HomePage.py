from selenium.webdriver.common.by import By

from pageobjcts.checkout import checkoutpage


class Homepage:
    def __init__(self, driver):
        self.driver = driver  # Store the WebDriver instance in the class

    def shopitems(self):
        # Use the WebDriver instance to find the element
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

        checkoutPage = checkoutpage(self.driver)
        return checkoutPage







    def getname(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='name'][type='text']")


    def getID(self):
        return self.driver.find_element(By.NAME, 'email')

    def getpass(self):
        return self.driver.find_element(By.ID, 'exampleInputPassword1')

    def checkbox(self):
        return self.driver.find_element(By.ID, 'exampleCheck1')

    def dropDown(self):
        return self.driver.find_element(By.ID, 'exampleFormControlSelect1')

    def radiobutton(self):
        return self.driver.find_element(By.ID, 'inlineRadio1')

    def submitbtn(self):
        return self.driver.find_element(By.XPATH, '//input[@type="submit"]')

    def successmsg(self):
        return self.driver.find_element(By.CLASS_NAME, 'alert-success')









