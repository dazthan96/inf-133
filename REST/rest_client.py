import requests

url ="http://localhost:8000/"

ruta_get = url +"lista_estudiantes"
get_response = requests.request(method="GET",url=ruta_get)
print(get_response.text)

ruta_post = url+"agrega_estudiante"
nuevo_estudiante_1={
    "nombre":"juan",
    "apellido":"perez",
    "carrera":"Ingenieria Agronomica",
}
requests.request(method="POST",url=ruta_post,json=nuevo_estudiante_1)


ruta_post = url+"agrega_estudiante"
nuevo_estudiante_2={
    "nombre":"luis",
    "apellido":"sanchez",
    "carrera":"Ingenieria Agronomica",
}
nuevo_estudiante_3={
    "nombre":"patricia",
    "apellido":"garcia",
    "carrera":"biologia",
}
nuevo_estudiante_4={
    "nombre":"alejandra",
    "apellido":"machicao",
    "carrera":"psicologia",
}
nuevo_estudiante_5={
    "nombre":"helen",
    "apellido":"varela",
    "carrera":"sociologia",
}
nuevo_estudiante_6={
    "nombre":"escarleth",
    "apellido":"castillo",
    "carrera":"biologia",
}
post_response =requests.request(method="POST",url=ruta_post,json=nuevo_estudiante_2)
post_response =requests.request(method="POST",url=ruta_post,json=nuevo_estudiante_3)
post_response =requests.request(method="POST",url=ruta_post,json=nuevo_estudiante_4)
post_response =requests.request(method="POST",url=ruta_post,json=nuevo_estudiante_5)
post_response =requests.request(method="POST",url=ruta_post,json=nuevo_estudiante_6)
print(post_response.text)
print("<----------------------------------------------------->")
ruta_get01=url+"buscar_nombre"
respuesta01=requests.request(method="GET",url=ruta_get01)
print(respuesta01.text)
print("<----------------------------------------------------->")
ruta_get02=url+"contar_carrera"
respuesta02=requests.request(method="GET",url=ruta_get02)
print(respuesta02.text)
print("<----------------------------------------------------->")
ruta_get_03=url+"total_estudiantes"
respuesta03=requests.request(method="GET",url=ruta_get_03)
print(respuesta03.text)