from zeep import Client
client =Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
client2 = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
resutl2 = client2.service.NumberToDollars(5)
result =client.service.NumberToWords(5)
print(result)
print(resutl2)