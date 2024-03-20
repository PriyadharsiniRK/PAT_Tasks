from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

#Launching URL
driver.get("https://www.saucedemo.com/")
sleep(5)

driver.maximize_window()

#wait
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

# printing cookies before logout
cookies_BeforeLogin= driver.get_cookies()
print("Cookies Before Login :",cookies_BeforeLogin)

#Iputing username.password
driver.find_element(by=By.ID, value="user-name").send_keys('standard_user')
sleep(3)

driver.find_element(by=By.ID, value="password").send_keys('secret_sauce')
sleep(3)
#Clicking on LogIn button
driver.find_element(by=By.ID, value="login-button").click()
sleep(3)
# printing cookies at login process
cookies_atloginProcess= driver.get_cookies()
print("Cookies created in Login process :",cookies_atloginProcess)

driver.find_element(by=By.ID, value="react-burger-menu-btn").click()
sleep(3)

driver.find_element(by=By.ID, value="logout_sidebar_link").click()
sleep(3)

# printing cookies after logout
cookies_AfterLogin= driver.get_cookies()
print("Cookies After Login :",cookies_AfterLogin)

# Close the browser
driver.quit()
