from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/Beelink-SER5-Computer-Display-Bluetooth/dp/B0C3VJGWSL/ref=sr_1_1_sspa?crid=G9S4AW54HEY2&keywords=pc&qid=1696601812&sprefix=%2Caps%2C569&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A3OHI25ZCHSGMQ")

price = driver.find_element("a-offscreen")
print(price.text)

# driver.close()
driver.quit()
