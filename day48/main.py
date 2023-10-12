from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://coinmarketcap.com/currencies/shiba-inu/")

price = driver.find_element(By.CSS_SELECTOR, ".sc-16891c57-0 ksCNvw base-text")
print(price.text)

# driver.close()
driver.quit()
