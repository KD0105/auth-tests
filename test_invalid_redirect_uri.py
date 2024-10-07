def test_invalid_redirect_uri():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://invalid.redirect.uri&response_type=code&scope=openid")

    driver.find_element(By.NAME, "login").send_keys("danilbeketov@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("danilbeketov@mail.ru")
    driver.find_element(By.NAME, "submit").click()

    error_message = driver.find_element(By.ID, "error_message").text
    assert "Ошибка редиректа" in error_message
    driver.quit()
