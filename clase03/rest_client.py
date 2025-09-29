import requests

urlBase = "http://localhost:8000/"

ruta_get_all = urlBase + "estudiantes"
result_get_all = requests.request(method="GET", url=ruta_get_all)
print(result_get_all.text)

ruta_carreras = urlBase+"carreras"
result_carreras = requests.request(method="GET", url=ruta_carreras)
print(result_carreras.text)

ruta_eco = urlBase + "estudiantes/Economia"
result_eco = requests.request(method="GET", url=ruta_eco)
print(result_eco.text)

ruta_post = urlBase + "estudiantes"
estudiantes ={
        "nombre":"Luis",
        "apellido":"Cabrera",
        "carrera":"Informatica"
    }
result_post = requests.request(method="POST", url=ruta_post, json=estudiantes)
estudiante = {
        "nombre":"Anabel",
        "apellido":"Huanca",
        "carrera":"Comunicacion Social"
    }
result_post = requests.request(method="POST", url=ruta_post, json=estudiante)
print(result_post.text)