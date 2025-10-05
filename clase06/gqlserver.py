from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema

class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()
    
estudiantes = [
    Estudiante(
        1,"Pedrito", "Garcia", "Ingenieria de Sistema"
    ),
    Estudiante(
        2, "Jose", "Lopez", "Arquitectura"
    )
]
class Query(ObjectType):               
    estudiantes = List(Estudiante)
    def resolve_estudiantes(root, info):
        print(estudiantes)
        return estudiantes
    
schema = Schema(query=Query)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    def do_POST(self):
        if self.path == "/graphql":
            content_length = int (self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no encontrada"})
            
def run_server(port = 8000):
    try:
        server_sddress = ("", port)
        httpd = HTTPServer(server_sddress, GraphQLRequestHandler)
        print(f"Servidor iniciado en http://localhost:{port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor")
        httpd.socket.close()
        
if __name__ == "__main__":
    run_server()