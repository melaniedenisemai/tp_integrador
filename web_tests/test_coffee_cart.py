from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://coffee-cart.app/"


def test_carga_inicial(driver):
    driver.get(URL)
    assert driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").is_displayed()
    assert "cart (0)" in driver.find_element(By.CSS_SELECTOR, "a[aria-label='Cart page']").text
    driver.save_screenshot("evidencias/ui1_carga_inicial.png")


def test_agregar_producto(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
    assert "cart (1)" in driver.find_element(By.CSS_SELECTOR, "a[aria-label='Cart page']").text
    assert "Total: $10.00" in driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").text
    driver.save_screenshot("evidencias/ui2_agregar_producto.png")


def test_compra_completa(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='Cappuccino']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
    driver.find_element(By.ID, "name").send_keys("Melanie")
    driver.find_element(By.ID, "email").send_keys("melanie@mail.com")
    driver.find_element(By.ID, "submit-payment").click()
    wait = WebDriverWait(driver, 10)
    assert wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, ".snackbar.success"), "Thanks for your purchase"))
    driver.save_screenshot("evidencias/ui3_compra_completa.png")
