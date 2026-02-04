from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class DeliveryVehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.package_delivered = 0
    
    def deliver(self):
        self.package_delivered +=1
        if self.package_delivered<self.capacity:
            
            return {
                "vehiculo": self.__class__.__name__,
                "Capacidad Maxima": self.capacity,
                "Entregas realizadas": self.package_delivered,
                "Mensaje":f"Le quedan {self.capacity - self.package_delivered} entregas"
            }
        else:
            return {
                "vehiculo": self.__class__.__name__,
                "Capacidad Maxima": self.capacity,
                "Entregas realizadas": self.package_delivered,
                "Mensaje": "Se ha alcanzado el limite de entregas"
            }
    
    
class Motorcycle(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity = 10)
    
class Drone(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=20)
    
vehicles = {}
class DeliverFactory:
    def create_delivery_vehicle(self, vehicle_type):
        if vehicle_type not in vehicles:
            if vehicle_type == "motorcycle":
                vehicles[vehicle_type]= Motorcycle()
            elif vehicle_type == "drone":
                vehicles[vehicle_type] = Drone()
            else:
                raise ValueError("Tipo de vehiculo de entrega no valido")
        return vehicles[vehicle_type]
class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path =="/delivery":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode("utf-8"))

            vehicle_type = request_data.get("vehicle_type")
            delivery_factory = DeliverFactory()
            delivery_vehicle = delivery_factory.create_delivery_vehicle(vehicle_type)

            response_data = delivery_vehicle.deliver()
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Ruta no encontrada")

def main():
    try:
        server_address = ("",8000)
        httpd = HTTPServer(server_address,DeliveryRequestHandler)
        print("Servidor en el puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()
if __name__ == "__main__":
    main()