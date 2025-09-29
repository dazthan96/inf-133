from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id" : 1,
        "nombre": "Juan",
        "apellido":"Perez",
        "carrera" : "Ingenieria de Sistemas"
    }
]
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path.startswith('/buscar_estudiante/'):
            id = str(self.path.split('/')[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["nombre"][0]==id), None
            )
            if estudiante:
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode('utf-8'))
        elif self.path.startswith("/contar_carreras"):
            carreras = set()
            for estudiante in estudiantes:
                carreras.add(estudiante["carrera"])
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(len(carreras)).encode('utf-8'))
        elif self.path.startswith("/total_estudiantes"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(len(estudiantes)).encode('utf-8'))
    def do_POST(self):
        if self.path == '/agregar_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes)+1
            estudiantes.append(post_data)
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no encontrada"}).encode('utf-8'))
            
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