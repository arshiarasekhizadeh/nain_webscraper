import os
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException , NoSuchElementException

WINDOW_SIZE = "1920,1080"
firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--no-sandbox")  
#firefox_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Firefox(options=firefox_options)


def get_product_data_de(products_links) :
    print('extracting data products data (de) ...')
    fields = ['link', 'name', 'size', 'category' , 'descrption' , 'price', 'carpet_id', 'thickness', 'manufacturing', 'warp', 'origin', 'pile' ,'age', 'weight', 'in_stock']
    if os.path.exists('output/data(de).csv') == False :
        with open('output/data(de).csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
    for link in products_links :
        driver.get(link)
        name = driver.find_element(By.XPATH , '/html/body/div[6]/div[2]/h1').text
        size = driver.find_element(By.XPATH , '/html/body/div[6]/div[2]/span').text
        category = driver.find_element(By.XPATH , '/html/body/div[6]/div[2]/div[1]').text
        category = category.replace(' ' , ', ')
        try :
            descrption = driver.find_element(By.XPATH , '/html/body/div[6]/div[2]/div[6]/p').text
        except NoSuchElementException : 
            descrption = ''
        try : 
            price = driver.find_element(By.XPATH , "//*[@class='block text-5xl font-bold']").text
        except NoSuchElementException : 
            price = driver.find_element(By.XPATH , "//*[@class='block text-5xl font-bold mt-5']").text
        data = driver.find_element(By.XPATH , "//*[@class='grid grid-cols-1 sm:grid-cols-2 text-sm leading-6']").text.split('\n')
        for d in data :
            if 'Teppich-Nr' in d :
                carpet_id = d
            if 'Dicke' in d :
                thickness = d
            if 'Verarbeitung' in d :
                manufacturing = d
            if 'Kette' in d :
                warp = d
            if 'Ursprung' in d :
                origin = d
            if 'Flor' in d :
                pile = d
            if 'Alter' in d :
                age = d
            if 'Gewicht' in d :
                weight = d
            if 'Anzahl auf Lager' in d :
                in_stock = d
        with open('output/data(de).csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writerows([{'link': link  , 'name': name , 'size': size , 'category' : category , 'descrption' : descrption , 'price': price , 'carpet_id': carpet_id , 'thickness': thickness , 'manufacturing': manufacturing , 'warp':  warp, 'origin' : origin , 'pile' : pile,'age': age, 'weight': weight , 'in_stock' : in_stock}])
    driver.quit()

