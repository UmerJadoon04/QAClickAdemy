from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to your chromedriver executable
service = Service(executable_path='C:/Users/Dell/Downloads/127.0.6533.72 chromedriver-win64/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get('https://qaclickacademy.github.io/protocommerce/')
driver.quit()
