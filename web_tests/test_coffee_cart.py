import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://coffee-cart.app/"


class TestCoffeeCart:

    def test_carga_inicial(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        #assert driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").is_displayed()
        #assert "cart (0)" in driver.find_element(By.CSS_SELECTOR, "a[aria-label='Cart page']").text
        assert driver.find_element(By.XPATH, "//div[@data-test='Espresso']").is_displayed()
        assert "cart (0)" in driver.find_element(By.XPATH, "//html/body/div/ul/li/a[@aria-label='Cart page']").text
        driver.save_screenshot("evidencias/ui1_carga_inicial.png")
        driver.quit()

    def test_agregar_producto(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        #driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
        #assert "cart (1)" in driver.find_element(By.CSS_SELECTOR, "a[aria-label='Cart page']").text
        #assert "Total: $10.00" in driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").text
        driver.find_element(By.XPATH, "//div[@data-test='Espresso']").click()
        assert "cart (1)" in driver.find_element(By.XPATH, "//a[@aria-label='Cart page']").text
        assert "Total: $10.00" in driver.find_element(By.XPATH, "//button[@data-test='checkout']").text
        driver.save_screenshot("evidencias/ui2_agregar_producto.png")
        driver.quit()


    def test_agregar_producto_con_mal_precio_total(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        #driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
        #assert "cart (1)" in driver.find_element(By.CSS_SELECTOR, "a[aria-label='Cart page']").text
        #assert "Total: $10.00" in driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").text
        driver.find_element(By.XPATH, "//div[@data-test='Espresso']").click()
        assert "cart (1)" in driver.find_element(By.XPATH, "//a[@aria-label='Cart page']").text
        assert not "Total: $1500.00" in driver.find_element(By.XPATH, "//button[@data-test='checkout']").text
        driver.save_screenshot("evidencias/ui2bis_agregar_producto_con_mal_precio_total.png")
        driver.quit()


    def test_compra_completa(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        #driver.find_element(By.CSS_SELECTOR, "[data-test='Espresso']").click()
        #driver.find_element(By.CSS_SELECTOR, "[data-test='Cappuccino']").click()
        #driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        driver.find_element(By.XPATH, "//div[@data-test='Espresso']").click()
        driver.find_element(By.XPATH, "//div[@data-test='Cappuccino']").click()
        driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()
        driver.find_element(By.ID, "name").send_keys("Melanie")
        driver.find_element(By.ID, "email").send_keys("melanie@mail.com")
        driver.find_element(By.ID, "submit-payment").click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, ".snackbar.success"), "Thanks for your purchase"))
        driver.save_screenshot("evidencias/ui3_compra_completa.png")
        driver.quit()


""" def test_unahur(self):
    driver.get("https://www.google.com")

    assert driver.title == "Google"

    caja = driver.find_element(By.XPATH, "//textarea[@name='q']")
    caja.send_keys("siu guarani unahur")
    caja.send_keys(Keys.ENTER)

    # Busco el link de UNAHUR en los resultados
    link = driver.find_element(By.XPATH, "//a[contains(@href,'servicios.unahur.edu.ar')]")
    assert link.is_displayed() """
