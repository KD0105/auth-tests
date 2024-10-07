from selenium import webdriver
from selenium.webdriver.common.by import By

def test_successful_authentication():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid")

    driver.find_element(By.NAME, "login").send_keys("danilbeketov@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("78965412Kd")
    driver.find_element(By.NAME, "submit").click()

    assert driver.current_url == "https://b2c.passport.rt.ru/account_b2c/login"
    driver.quit()
