from selenium import webdriver
from selenium.webdriver.common.by import By

def test_successful_authentication():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid")

    driver.find_element(By.NAME, "login").send_keys("valid_username")
    driver.find_element(By.NAME, "password").send_keys("valid_password")
    driver.find_element(By.NAME, "submit").click()

    assert driver.current_url == "https://b2c.passport.rt.ru/account_b2c/login"
    driver.quit()
