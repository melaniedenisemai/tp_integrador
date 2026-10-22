import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    opciones = webdriver.ChromeOptions()
    opciones.add_argument("--headless=new")  # sin ventana, borrar esta linea para ver el navegador
    driver = webdriver.Chrome(options=opciones)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
