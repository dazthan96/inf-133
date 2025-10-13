import requests

url = "http://localhost:8000/"
ruta_get_all = url + "estudiantes"
response_all = requests.request(method="GET", url=ruta_get_all)
print(response_all.text)


ruta_post = url + "estudiantes"
estudiante = {
    "nombre":"Juan",
    "apellido":"Perez",
    "carrera":"Ingenieria Agronomica"
}

post_response = requests.request(method="POST", url=ruta_post, json=estudiante)
print(post_response.text)

ruta_get_est = url + "estudiantes?nombre=Pedrito"
get_response = requests.request("GET", ruta_get_est)
print(get_response.text)

ruta_get_est_id = url + "estudiantes/3"
get_response_id = requests.request("GET", ruta_get_est_id)
print(get_response_id.text)

ruta_del_est_id = url + "estudiantes/3"
del_response_id = requests.request("DELETE", ruta_del_est_id)
print(del_response_id.text)