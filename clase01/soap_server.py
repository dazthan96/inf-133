from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def Saludar(nombre:str):
    return f"¡Hola {nombre}!"
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trcae=True,
    ns=True
)
def SumarDosNumeros(a:int, b: int):
    return f"{a+b}"

def EsPalindromo(word:str):
    if word==word[::-1]:
        return "es palindromo"
    else:
        return "no es palindromo" 

dispatcher.register_function(
    "Saludar",
    Saludar,
    returns={"saludo":str},
    args={"nombre":str}
)
dispatcher.register_function(
    "Sumar",
    SumarDosNumeros,
    returns={"result":str},
    args={"a":int, "b":int}
)
dispatcher.register_function(
    "Palindromo",
    EsPalindromo,
    returns={"result":str},
    args={"word":str}
)
server = HTTPServer(("0.0.0.0",8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever() 