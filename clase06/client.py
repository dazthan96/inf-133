import requests
query = """
    {
        hello
    }
"""
consulta2 = """
    {
        goodbye
    }
"""

url = "http://localhost:8000/graphql"
response = requests.post(url, json={'query':query})

response2 = requests.post(url, json ={'query':consulta2})

print(response.text)
print(response2.text)