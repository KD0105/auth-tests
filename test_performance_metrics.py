import time

def test_performance():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid")

    start_time = time.time()
    driver.find_element(By.NAME, "login").send_keys("danilbeketov@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("78965412Kd")
    driver.find_element(By.NAME, "submit").click()
    end_time = time.time()

    assert (end_time - start_time) < 2, "Время отклика превышает 2 секунды"
    driver.quit()
