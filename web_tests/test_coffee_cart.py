from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://coffee-cart.app/"


def test_carga_inicial(driver):
    driver.get(URL)
    espresso = driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']")
    assert espresso.is_displayed()
    carrito = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Cart page']")
    assert "cart (0)" in carrito.text
    driver.save_screenshot("evidencias/ui1_carga_inicial.png")


def test_agregar_producto(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
    # la cantidad aumenta en uno
    carrito = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Cart page']")
    assert "cart (1)" in carrito.text
    # el total refleja la compra (el espresso cuesta $10.00)
    total = driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']")
    assert "Total: $10.00" in total.text
    driver.save_screenshot("evidencias/ui2_agregar_producto.png")


def test_compra_completa(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='Cappuccino']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
    driver.find_element(By.ID, "name").send_keys("Juan Perez")
    driver.find_element(By.ID, "email").send_keys("juan@mail.com")
    driver.find_element(By.ID, "submit-payment").click()
    mensaje = (By.CSS_SELECTOR, ".snackbar.success")
    espera = WebDriverWait(driver, 10)
    assert espera.until(EC.text_to_be_present_in_element(mensaje, "Thanks for your purchase"))
    driver.save_screenshot("evidencias/ui3_compra_completa.png")
