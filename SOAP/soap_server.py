from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "hola, {}".format(nombre)

def sumaDosNumeros(num1,num2):
    return num1+num2

def esPalindromo(cadena):
    if(cadena==cadena[::-1]):
        return True
    return False

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo":str},
    args={"nombre":str},
)

dispatcher.register_function(
    "SumaDosNumeros",
    sumaDosNumeros,
    returns={"resultado":int},
    args={"num1":int,"num2":int},
)

dispatcher.register_function(
    "CadenaPalindromo",
    esPalindromo,
    returns={"resultado":bool},
    args={"cadena":str},
)

server =HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher=dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()