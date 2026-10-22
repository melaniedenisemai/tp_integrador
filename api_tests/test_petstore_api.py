import pytest
import requests

URL = "https://petstore.swagger.io/v2"


def test_crear_mascota():
    mascota = {"id": 987654, "name": "Tony", "photoUrls": [], "status": "available"}
    respuesta = requests.post(URL + "/pet", json=mascota)
    assert respuesta.status_code == 200
    # json que tiene que devolver la API (agrega el campo tags vacio)
    esperado = {"id": 987654, "name": "Tony", "photoUrls": [], "tags": [], "status": "available"}
    assert respuesta.json() == esperado


def test_consultar_mascota():
    # primero se crea la mascota para que este test no dependa del otro
    mascota = {"id": 987654, "name": "Tony", "photoUrls": [], "status": "available"}
    requests.post(URL + "/pet", json=mascota)

    respuesta = requests.get(URL + "/pet/987654")
    assert respuesta.status_code == 200
    esperado = {"id": 987654, "name": "Tony", "photoUrls": [], "tags": [], "status": "available"}
    assert respuesta.json() == esperado


def test_mascota_inexistente():
    # el id 0 no existe, tiene que dar error 404
    respuesta = requests.get(URL + "/pet/0")
    assert respuesta.status_code == 404
    esperado = {"code": 1, "type": "error", "message": "Pet not found"}
    assert respuesta.json() == esperado
