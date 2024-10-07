def test_state_parameter():
    state = "test_state"
    driver = webdriver.Chrome()
    driver.get(f"https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state={state}")

    driver.find_element(By.NAME, "login").send_keys("danilbeketov@mail.ru")
    driver.find_element(By.NAME, "password").send_keys("78965412Kd")
    driver.find_element(By.NAME, "submit").click()

    # Assuming state is returned in the URL or as part of a response
    assert state in driver.current_url or driver.find_element(By.ID, "state_value").text == state
    driver.quit()
