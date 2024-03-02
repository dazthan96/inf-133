from zeep import Client

client =Client("http://localhost:8000")
result01 = client.service.Saludar(nombre="Alberto")
print(result01)

result02 = client.service.SumaDosNumeros(num1=1,num2=3)
print(result02)

result03 = client.service.CadenaPalindromo(cadena="alberto")
print(result03)
