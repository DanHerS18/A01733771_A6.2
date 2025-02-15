# hotel_system.py

class Hotel:
    def __init__(self, hotel_id, name, location, rooms_available):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def reserve_room(self):
        """Reserva una habitación si está disponible."""
        if self.rooms_available > 0:
            self.rooms_available -= 1
            return True
        return False

    def cancel_reservation(self):
        """Cancela una reserva y aumenta la disponibilidad de habitaciones."""
        self.rooms_available += 1


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email


class Reservation:
    def __init__(self, reservation_id, customer, hotel):
        """Crea una reserva asociada a un cliente y un hotel."""
        self.reservation_id = reservation_id
        self.customer = customer
        self.hotel = hotel

    def __str__(self):
        return f"Reserva ID: {self.reservation_id}, Cliente: {self.customer.name}, Hotel: {self.hotel.name}"

# Crear instancias de Hotel y Customer
def create_example_usage():
    hotel1 = Hotel(hotel_id=1, name="Hotel ABC", location="New York", rooms_available=5)
    customer1 = Customer(customer_id=1, name="John Doe", email="john.doe@example.com")

    # Reservar una habitación
    if hotel1.reserve_room():
        print(f"Reserva exitosa para {customer1.name} en {hotel1.name}")

    # Crear una instancia de Reservation
    reservation1 = Reservation(reservation_id=1, customer=customer1, hotel=hotel1)
    print(reservation1)

    # Cancelar una reserva
    hotel1.cancel_reservation()
    print(f"Habitaciones disponibles después de cancelación: {hotel1.rooms_available}")

# Llamada a la función para demostrar la interacción entre las clases
create_example_usage()
