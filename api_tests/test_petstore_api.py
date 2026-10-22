import requests

URL = "https://petstore.swagger.io/v2"


def test_crear_mascota():
    mascota = {"id": 987654, "name": "Tony", "photoUrls": [], "status": "available"}
    respuesta = requests.post(URL + "/pet", json=mascota)
    assert respuesta.status_code == 200
    assert respuesta.json()["name"] == "Tony"


def test_buscar_mascotas_disponibles():
    respuesta = requests.get(URL + "/pet/findByStatus", params={"status": "available"})
    assert respuesta.status_code == 200
    assert len(respuesta.json()) > 0


def test_mascota_inexistente():
    # el id 0 no existe, tiene que dar error 404
    respuesta = requests.get(URL + "/pet/0")
    assert respuesta.status_code == 404
