# TP Integrador - Testing automatizado

Trabajo practico con 9 tests automatizados en Python:

- 3 tests unitarios (pytest) sobre la funcion FizzBuzz
- 3 tests de API (pytest + requests) sobre [Petstore](https://petstore.swagger.io)
- 3 tests de UI (pytest + Selenium) sobre [Coffee Cart](https://coffee-cart.app/)

## Estructura

```text
tp_integrador/
├── unit_tests/
├── api_tests/
├── web_tests/
├── evidencias/
├── reportes/
├── pytest.ini
├── requirements.txt
└── README.md
```

## Instalacion

Hace falta tener Python y Google Chrome instalados.

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Como ejecutar

Todos los tests juntos:

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

### Unitarios (FizzBuzz)

| ID | Caso | Resultado esperado |
|----|------|--------------------|
| UT-01 | fizzbuzz(6) | 'Fizz' |
| UT-02 | fizzbuzz(10) | 'Buzz' |
| UT-03 | fizzbuzz(15) | 'FizzBuzz' |

### API (Petstore)

| ID | Caso | Resultado esperado |
|----|------|--------------------|
| API-01 | POST /pet (crear una mascota) | codigo 200 y el json de la mascota |
| API-02 | GET /pet/987654 (la mascota creada antes) | codigo 200 y el json de la mascota |
| API-03 | GET /pet/0 (no existe) | codigo 404 y el mensaje "Pet not found" |

### UI (Coffee Cart)

| ID | Caso | Resultado esperado |
|----|------|--------------------|
| UI-01 | Abrir la pagina | se ve el catalogo y el carrito dice `cart (0)` |
| UI-02 | Agregar un Espresso | el carrito dice `cart (1)` y el total es $10.00 |
| UI-02-bis | Agregar un Espresso | el carrito dice `cart (1)` y el total NO es $1500 |
| UI-03 | Comprar Espresso y Cappuccino completando nombre y email | aparece el mensaje "Thanks for your purchase" |

## Evidencias

Los tests de UI guardan una captura de pantalla en la carpeta `evidencias/`.
