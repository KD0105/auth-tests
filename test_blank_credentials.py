def test_empty_fields():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid")

    driver.find_element(By.NAME, "submit").click()

    error_message = driver.find_element(By.ID, "error_message").text
    assert "Введите логин и пароль" in error_message
    driver.quit()
