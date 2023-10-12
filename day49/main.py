from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.amazon.com/Beelink-SER5-Computer-Display-Bluetooth/dp/B0C3VJGWSL/ref=sr_1_1_sspa?crid=G9S4AW54HEY2&keywords=pc&qid=1696601812&sprefix=%2Caps%2C569&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A3OHI25ZCHSGMQ")

price = wait.until(EC.presence_of_element_located(
    driver.find_element(By.CSS_SELECTOR, ".offscreen")))

print(price.text)

driver.quit()
