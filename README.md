# TP Integrador - Testing automatizado

Trabajo practico con 9 tests automatizados en Python:

- 3 tests unitarios (pytest) sobre la funcion FizzBuzz
- 3 tests de API (pytest + requests) sobre [Petstore](https://petstore.swagger.io)
- 3 tests de UI (pytest + Selenium) sobre [Coffee Cart](https://coffee-cart.app/)

## Estructura

```text
tp_integrador/
├── .github/workflows/main.yml   # GitHub Actions
├── unit_tests/                  # fizzbuzz y sus tests
├── api_tests/                   # tests de la API
├── web_tests/                   # tests de Selenium
├── evidencias/                  # capturas de pantalla
├── reportes/                    # reporte HTML
├── informe_final.md             # informe final del trabajo
├── pytest.ini
├── requirements.txt
└── README.md
```

## Instalacion

Hace falta tener Python y Google Chrome instalados.

```bash
cd tp_integrador
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

(en Linux/Mac el activate es `source .venv/bin/activate`)

## Como ejecutar

Todos los tests juntos, genera el reporte en `reportes/reporte.html`:

```bash
pytest
```

Por separado:

```bash
pytest unit_tests
pytest api_tests
pytest web_tests
```

## Casos de prueba

### Unitarios

| ID | Caso | Resultado esperado |
|----|------|--------------------|
| UT-01 | fizzbuzz(6) | 'Fizz' |
| UT-02 | fizzbuzz(10) | 'Buzz' |
| UT-03 | fizzbuzz(15) | 'FizzBuzz' |

### API

| ID | Caso | Resultado esperado |
|----|------|--------------------|
| API-01 | POST /pet (crear mascota) | codigo 200 y el nombre enviado |
| API-02 | GET /pet/findByStatus?status=available | codigo 200 y lista con mascotas |
| API-03 | GET /pet/0 (no existe) | codigo 404 |

### UI

| ID | Caso | Resultado esperado |
|----|------|--------------------|
| UI-01 | Carga inicial | se ve el catalogo y el carrito dice `cart (0)` |
| UI-02 | Agregar un Espresso | el carrito dice `cart (1)` y el total es $10.00 |
| UI-03 | Comprar Espresso y Cappuccino completando nombre y email | aparece el mensaje "Thanks for your purchase" |

## Resultados

- Reporte: `reportes/reporte.html`
- Capturas: carpeta `evidencias/` (si un test web falla se guarda una captura `ERROR_...png`)
- Informe final: `informe_final.md`
- Los tests se ejecutan solos en cada push con GitHub Actions.
