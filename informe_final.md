# Informe Final - TP Integrador

## 1. Descripcion de los sistemas seleccionados

**FizzBuzz (pruebas unitarias):** funcion en Python (`unit_tests/fizzbuzz.py`) que recibe un numero y devuelve `'Fizz'` si es divisible por 3, `'Buzz'` si es divisible por 5, `'FizzBuzz'` si es divisible por ambos, o el mismo numero en otro caso.

**Petstore (pruebas de API):** API REST publica de ejemplo de Swagger (https://petstore.swagger.io/v2). Permite crear, buscar y consultar mascotas.

**Coffee Cart (pruebas de UI):** aplicacion web de una cafeteria (https://coffee-cart.app/). Se pueden agregar cafes al carrito, ver el total y hacer el checkout completando nombre y email.

## 2. Estrategia de testing

- **Unitarias:** se prueba la funcion aislada, un caso por cada regla (multiplo de 3, de 5 y de ambos).
- **API:** se prueban peticiones reales con `requests` y se valida el codigo de estado y el json de la respuesta. Se cubre un caso de exito al crear, uno de busqueda, uno de consulta de una mascota existente y uno de error (404). El test de consulta crea antes la mascota que va a pedir, para no depender de otros tests ni de lo que haya en el servidor.
- **UI:** se automatiza el recorrido de un usuario con Selenium: carga inicial, agregar un producto y compra completa. Se usan selectores estables (`data-test`, `aria-label` e `id`).
- Los tres niveles se ejecutan con un unico comando (`pytest`) y generan un reporte HTML.
- Cuando un test web falla se guarda una captura de pantalla automaticamente en `evidencias/`.

## 3. Casos de prueba disenados

| ID | Tipo | Caso | Resultado esperado |
|----|------|------|--------------------|
| UT-01 | Unitario | fizzbuzz(6) | 'Fizz' |
| UT-02 | Unitario | fizzbuzz(10) | 'Buzz' |
| UT-03 | Unitario | fizzbuzz(15) | 'FizzBuzz' |
| API-01 | API | POST /pet con una mascota nueva | codigo 200 y el json con los datos enviados (la API agrega `tags: []`) |
| API-02 | API | GET /pet/findByStatus?status=available | codigo 200 y lista con mascotas |
| API-03 | API | GET /pet/987654 (mascota creada antes en el mismo test) | codigo 200 y el json completo de la mascota |
| API-04 | API | GET /pet/0 (no existe) | codigo 404 y el json `{"code": 1, "type": "error", "message": "Pet not found"}` |
| UI-01 | UI | Carga inicial | se ve el catalogo y el carrito dice `cart (0)` |
| UI-02 | UI | Agregar un Espresso | el carrito dice `cart (1)` y el total es $10.00 |
| UI-03 | UI | Comprar Espresso y Cappuccino completando nombre y email | aparece "Thanks for your purchase" |

## 4. Herramientas utilizadas

| Herramienta | Uso |
|-------------|-----|
| Python | lenguaje de los tests |
| pytest | ejecucion de los tests |
| requests | peticiones HTTP a la API |
| Selenium + Chrome | automatizacion del navegador |
| pytest-html | reporte HTML |
| GitHub Actions | ejecucion automatica en cada push |
| Git | control de versiones |

## 5. Resultados obtenidos

- Tests ejecutados: **10**
- Aprobados: **10**
- Fallidos: **0**
- Tiempo total aproximado: 18 segundos
- Reporte: `reportes/reporte.html`
- Evidencias: `evidencias/ui1_carga_inicial.png`, `ui2_agregar_producto.png` y `ui3_compra_completa.png`
- Se verifico tambien que, si un test web falla, se genera una captura `ERROR_<nombre del test>.png` en `evidencias/`.
- Pipeline de GitHub Actions (workflow "Tests"): se ejecuta en cada push a `main`. En la ultima ejecucion corrieron los 10 tests y todos pasaron (`10 passed`). El reporte HTML y las evidencias quedan disponibles en `/reportes` y `/evidencias`.

## 6. Incidencias encontradas

No se encontraron defectos en las aplicaciones probadas, pero si surgieron estas observaciones durante el desarrollo:

1. **Formulario de pago:** si se intenta enviar sin completar los campos, el aviso es la validacion nativa del navegador (atributo `required`) y no un mensaje propio de la aplicacion. 

## 7. Mejoras propuestas

- Usar **datos externos** (CSV o JSON) para probar varias combinaciones de cafes y precios.
- Agregar mas casos de UI: eliminar productos, validacion de campos obligatorios y descuentos emergentes.
- Agregar mas casos de API: actualizar y borrar mascotas.
