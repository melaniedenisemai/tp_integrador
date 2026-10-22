import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    opciones = webdriver.ChromeOptions()
    # el navegador se abre sin ventana (para verlo, borrar la siguiente linea)
    opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1366,900")
    driver = webdriver.Chrome(options=opciones)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Si un test web falla, se guarda una captura en evidencias/
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            driver.save_screenshot("evidencias/ERROR_" + item.name + ".png")
