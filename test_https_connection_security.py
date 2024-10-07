def test_https_redirect():
    driver = webdriver.Chrome()
    driver.get("http://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid")

    assert driver.current_url.startswith("https://")
    driver.quit()
