from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=r'/usr/local/bin/chromedriver')
driver.get("https://www.directliquidation.com/electronics/?s=&idx=dl_prod_posts_product_end_date_ts_asc&page=10")


delay = 15 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/section/div[2]/div/div[2]/div/div[1]')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took more than 20 seconds")

parentElement = driver.find_element(By.XPATH, '//*[@id="content"]/section/div[2]/div/div[2]/div/div[1]')
elementList = parentElement.find_elements(By.CSS_SELECTOR, ":scope > div")


for product in elementList:

    title = product.find_element(By.CSS_SELECTOR, ".product-card__details .product-card__details-title").text
    bid = product.find_element(By.CSS_SELECTOR, ".product-card__details .product-card__details-price .amount").text
    time = product.find_element(By.CSS_SELECTOR, ".product-card__details .data-countdown").text
    print(title)
    print(bid)
    print(time)

driver.save_screenshot('screenshot.png')
# driver.quit()