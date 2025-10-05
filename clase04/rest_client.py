import requests

urlBase = "http://localhost:8000/"

ruta_get_all = urlBase + "estudiantes"
result_get_all = requests.request(method="GET", url=ruta_get_all)
print(result_get_all.text)
ruta_est_id = urlBase + "estudiantes/1"
retult_est_id = requests.request(method="GET", url=ruta_est_id)
print(retult_est_id.text)

ruta_get_carreras = urlBase + "carreras"
result_get_carreras = requests.request(method="GET", url = ruta_get_carreras)
print(result_get_carreras.text)

ruta_est_carrera = urlBase + "estudiantes/Economia"
result_est_carrera = requests.request(method="GET", url= ruta_est_carrera)
print(result_est_carrera.text)

nuevo_estudiante = {
    "nombre":"Pedro",
    "apellido":"Picapiedra",
    "carrera": "Sociologia"
}

ruta_new_est = urlBase + "estudiantes"
result_new_est = requests.request(method="POST",url=ruta_new_est, json=nuevo_estudiante)
print(result_new_est.text)

result_all_est = requests.request(method="GET", url=ruta_get_all)
print(result_all_est.text)