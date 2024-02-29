import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


WINDOW_SIZE = "1920,1080"
firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--no-sandbox")  
#firefox_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Firefox(options=firefox_options)

extended_wait = 1200
def get_product_links(url) :
    driver.get(url)
    time.sleep(10)
    try:
        WebDriverWait(driver, extended_wait).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-content.col-span-full'))
        )

        product_links = []
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.main-content.col-span-full')
        for element in elements:
            products = element.find_elements(By.TAG_NAME , 'a')
            for product in products:
                product_links.append(product.get_attribute('href'))

        filter_product_links = list(filter(lambda item: item is not None, product_links))

        for link in filter_product_links:
            if link == '' :
                continue
            with open('nl/products(nl).txt' , 'a') as file :
                if re.match(r'https://www.naintrading.nl/oosterse-tapijten/.*-p-[0-9]*.html' , link) :
                    file.write(f'{link}\n')
                file.close()
        with open('nl/products(nl).txt' , 'r') as read_file :
            res = read_file.readlines()
    except TimeoutException:
        print("Timed out waiting for page to load")

    driver.quit()
    return res


