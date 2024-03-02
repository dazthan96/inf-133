from zeep import Client
client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result01 = client.service.NumberToWords(5)
print("De numero a letras: ", result01)

result02 = client.service.NumberToDollars(10)
print("Convertir a dolares: ",result02)