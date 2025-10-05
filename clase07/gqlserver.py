from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation

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

class Query (ObjectType):
    estudiantes = List(Estudiante)
    estudiante_por_id = Field(Estudiante, id =Int())
    estudiante_por_carrera = List(Estudiante, carrera=String())
    estudiante_por_nombre_apellido = Field(Estudiante, nombre = String(), apellido = String())
    #para returna una lista de busqueda por un parametro, en la funcion resolve se debe llamar a una copia completa de la lista del objeto original para despues hacer el filtrado de resultado 
    def resolve_estudiantes(root, info):
        print(estudiantes)
        return estudiantes
    
    def resolve_estudiante_por_id(root, info, id):
        for estudiante in estudiantes:
            if estudiante.id == id:
                return estudiante
        return None
    
    def resolve_estudiante_por_carrera(root, info, carrera):
        students = estudiantes
        return [e for e in students if e.carrera == carrera]
        
    def resolve_estudiante_por_nombre_apellido(root, info, nombre, apellido):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre and estudiante.apellido == apellido:
                return estudiante
        return None
class CrearEstudiante(Mutation):
    class Arguments:
        nombre = String()
        apellido = String()
        carrera = String()
    estudiante = Field(Estudiante)
    def mutate(root, info, nombre, apellido, carrera):
        nuevo_estudiante = Estudiante(
            id = len(estudiantes) +1, 
            nombre = nombre,
            apellido = apellido,
            carrera = carrera 
        )
        estudiantes.append(nuevo_estudiante)
        return CrearEstudiante(estudiante = nuevo_estudiante)
    
class DeleteEstudiante(Mutation):
    class Arguments:
        id = Int()
    estudiante = Field(Estudiante)
    def mutate(root, info, id):
        for i, estudiante in enumerate(estudiantes):
            if estudiante.id == id:
                estudiantes.pop(i)
                return DeleteEstudiante(estudiante = estudiante)
        return None
class UpdateEstudiante(Mutation):
    class Arguments:
        nombre = String()
        apellido = String()
        carrera = String()
    estudiante = Field(Estudiante)
    def mutate(root, info, nombre, apellido, carrera):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre and estudiante.apellido==apellido:
                estudiante.carrera =carrera
                return UpdateEstudiante(estudiante = estudiante)
        return None
class Mutations(ObjectType):
    crear_estudiante = CrearEstudiante.Field()
    delete_estudiante = DeleteEstudiante.Field()
    update_estudiante = UpdateEstudiante.Field()
schema = Schema(query=Query, mutation=Mutations)

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