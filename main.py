import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
product=input("inter product to be search")
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]div/button")
time.sleep(1)
driver.find_element_by_name("q").send_keys(product)
time.sleep(1)
driver.find_element_by_class_name("L0Z3Pu").click()
time.sleep(1)
driver.close()
print("search successful")
