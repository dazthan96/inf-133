import requests


url = 'http://localhost:8000/graphql'

query = """
    {
        estudiantes {
            id
            nombre
            apellido
            carrera
        }
    }
"""
query2  = """
    {
        estudiantes{
            nombre
        }
    }
"""
query3 = """
    {
        estudiantes{
            nombre
            apellido
        }
    }
"""

response = requests.post(url, json={'query':query})
response2 = requests.post(url, json={'query':query2})
response3 = requests.post(url, json={'query':query3})
print(response.text)
print(response2.text)
print(response3.text)