import requests
urlBase= "http://localhost:8000/"
ruta_url = urlBase + "lista_estudiantes"
get_response = requests.request(method="GET",url=ruta_url)
print(get_response.text)

ruta_post = urlBase +"agregar_estudiante"
estudiante = {
    "nombre":"Pablo",
    "apellido" : "Cabrera",
    "carrera":"Ingenieria de Sistemas"
}
post_response = requests.request(method="POST", url=ruta_post, json=estudiante)
print(post_response.text)

ruta_get_char = urlBase+"buscar_estudiante/P"
get_response_char = requests.request(method="GET", url=ruta_get_char)
print(get_response_char.text)

ruta_get_size = urlBase + "contar_carreras"
get_response_size = requests.request(method="GET", url=ruta_get_size)
print(get_response_size.text)

ruta_get_total = urlBase + "total_estudiantes"
get_response_total = requests.request(method="GET", url=ruta_get_total)
print(get_response_total.text)