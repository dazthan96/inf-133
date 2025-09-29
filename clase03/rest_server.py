from http.server import BaseHTTPRequestHandler, HTTPServer
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
    def do_GET(self):
        if self.path.startswith("/estudiantes/"):
            carrera = str(self.path.split("/")[-1])
            estudiante=[]
            for e in estudiantes:
                if e["carrera"] == carrera:
                    estudiante.append(e)
            if estudiante:
                self.send_response(200)
                self.send_header("Content-type","application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        elif self.path.startswith("/estudiantes"):
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path.startswith("/carreras"):
            carreras = set()
            for estudiante in estudiantes:
                carreras.add(estudiante["carrera"])
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(list(carreras)).encode("utf-8"))
    def do_POST(self):
        if self.path == "/estudiantes":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"]= len(estudiantes)+1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            
        
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