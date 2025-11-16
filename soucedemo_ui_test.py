import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")

user_name=driver.find_element(By.XPATH,".//input[@id='user-name']")
user_name.clear()
user_name.send_keys("standard_user")

password=driver.find_element(By.XPATH,".//input[@id='password']")
password.clear()
password.send_keys("secret_sauce")

login_button=driver.find_element(By.XPATH,".//input[@id='login-button']")
login_button.click()

add_to_cart=driver.find_element(By.XPATH,".//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart.click()

cart_list=driver.find_element(By.XPATH,".//a[contains(@class,'shopping_cart_link')]")
cart_list.click()



title=driver.find_element(By.XPATH,".//div[contains(@class,'inventory_item_name')]")


print("Product name is:",title.text)


menu=driver.find_element(By.XPATH,".//button[contains(.,'Open Menu')]")
menu.click()



logout=driver.find_element(By.XPATH,".//a[@id='logout_sidebar_link']")
logout.click()
