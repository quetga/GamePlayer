from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('/Users/jaquetwatkins/Desktop/Development/chromedriver 4')
driver = webdriver.Chrome(service=s)

driver.get("https://www.amazon.com")

driver.quit()
