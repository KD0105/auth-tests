def test_page_availability():
    driver = webdriver.Chrome()
    driver.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid")

    assert "Логин" in driver.page_source
    assert "Пароль" in driver.page_source
    driver.quit()
