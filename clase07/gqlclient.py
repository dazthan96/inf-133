import requests

url = "http://localhost:8000/graphql"

# query = """
#     {
#         estudiantePorId(id:2){
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# """
# query2 = """
#     {
#         estudiantePorCarrera(carrera:"Arquitectura"){
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# """
# query3 = """
#     {
#         estudiantePorNombreApellido(nombre:"Jose", apellido:"Lopez"){
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# """
# #para realizar el filtrado de resultados por busqueda de parametros, debemos realizar la consulta de parametro como si no existiera comillas triples en el parametro de busqueda

# response1 = requests.post(url, json={'query':query})
# response2 = requests.post(url, json={'query': query2})
# response3 = requests.post(url, json={'query':query3})
# print(response1.text)
# print(response2.text)
# print(response3.text)

# query_crear="""
# mutation{
#     crearEstudiante(nombre:"Raiza", apellido:"Quiroga", carrera:"Biologia"){
#         estudiante{
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# }
# """
# query_crear1="""
# mutation{
#     crearEstudiante(nombre:"Rosmery", apellido:"Cari", carrera:"Arquitectura"){
#         estudiante{
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# }
# """
# query_crear2="""
# mutation{
#     crearEstudiante(nombre:"Victor", apellido:"Cabrera", carrera:"Arquitectura"){
#         estudiante{
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# }
# """
# query_crear3="""
# mutation{
#     crearEstudiante(nombre:"Ariadne", apellido:"Quiroz", carrera:"Arquitectura"){
#         estudiante{
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# }
# """
# response_mutation = requests.post(url, json={'query':query_crear})
# response_mutation1 = requests.post(url, json={'query':query_crear1})
# response_mutation2 = requests.post(url, json={'query':query_crear2})
# response_mutation3 = requests.post(url, json={'query':query_crear3})
# print(response_mutation1.text)
# print(response_mutation2.text)
# print(response_mutation3.text)
# print(response_mutation.text)
# responseArq = requests.post(url, json={'query': query2})
# print(responseArq.text)

# query_eliminar="""
# mutation{
#     deleteEstudiante(id:3){
#         estudiante{
#             id
#             nombre
#             apellido
#             carrera
#         }
#     }
# }
# """
# response_delete = requests.post(url, json = {'query':query_eliminar})
# print(response_delete.text)

query_all ="""
    {
        estudiantes{
        id
        nombre
        apellido
        carrera
        }
    }
"""
lista_actual = requests.post(url, json={'query':query_all})
print(lista_actual.text)
query_actualizar = """
mutation{
    updateEstudiante(nombre:"Jose", apellido:"Lopez", carrera:"Arquitectura"){
        estudiante{
            id
            nombre
            apellido
            carrera
        }
    }
    
}
"""

response_update = requests.post(url, json={'query':query_actualizar})
print(response_update.text)
response_all = requests.post(url, json={'query':query_all})
print(response_all.text)

query_eliminar="""
mutation{
    deleteEstudiante(carrera:"Arquitectura"){
        estudiante{
            id
            nombre
            apellido
            carrera
        }
    }
}
"""
response_delete = requests.post(url, json = {'query':query_eliminar})
print(response_delete.text)

response_all = requests.post(url, json={'query':query_all})
print(response_all.text)