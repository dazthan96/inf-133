from zeep import Client
client = Client(
    "http://localhost:8000/"
)
result = client.service.Saludar(nombre="Tatiana")
result2 = client.service.Sumar(a=5, b=6)
result3 = client.service.Palindromo(word="oso")
print(result)
print(result2)
print(result3)