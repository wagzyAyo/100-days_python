from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://coinmarketcap.com/currencies/shiba-inu/")

# Use an explicit wait to wait for the element to be present
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
price = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, ".sc-16891c57-0.ksCNvw.base-text")))

print(price.text)

driver.quit()
