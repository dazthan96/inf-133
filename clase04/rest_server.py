from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "nombre":"Juan",
        "apellido":"Perez",
        "carrera":"Economia",
        "id":1
    },
    {
        "nombre":"Pablo",
        "apellido":"Marmol",
        "carrera":"Matematica",
        "id":2
    },
    {
        "nombre":"Rosmery",
        "apellido":"Cari",
        "carrera":"Trabajo Social",
        "id":3
    },
    {
        "nombre":"Victor",
        "apellido":"Roman",
        "carrera":"Economia",
        "id":4
    }
]
class RESTRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
    
    def estudiantesCarrera(self, carrera):
        return list(estudiante for estudiante in estudiantes if estudiante["carrera"]==carrera)
    
    def carreras(self):
        return list(set(est["carrera"] for est in estudiantes))
    
    def estudiante_id(self, id):
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"]==id), None
        )
        
    def do_GET(self):
        if self.path == '/estudiantes':
            self.response_handler(200, estudiantes)
        elif self.path.startswith("/estudiantes/"):
            query = self.path.split("/")[-1]
            try:
                query=int(query)
            except:
                query=query
            print(type(query))
            if type(query) == str:
                estudiantes = self.estudiantesCarrera(query)
                if estudiantes:
                    self.response_handler(200, estudiantes)
                else:
                    self.response_handler(204, [])
            elif type(query)== int:
                estudiante = self.estudiante_id(query)
                if estudiante:
                    self.response_handler(200, estudiante)
                else:
                    self.response_handler(204, [])
        
        if self.path == '/carreras':
            carreras = self.carreras()
            if carreras:
                self.response_handler(200, carreras )
            else:
                self.response_handler(204, [])
    def do_POST(self):
        if self.path =="/estudiantes":
            data = self.read_data()
            data["id"] = len(estudiantes)+1
            estudiantes.append(data)
            self.response_handler(201, estudiantes)
        else:
            self.response_handler(404, "Ruta no Encontrada")
def run_server(port=8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando el Servidor")
        httpd.socket.close()
        
if __name__=='__main__':
    run_server()