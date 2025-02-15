import unittest
from hotel_system import Hotel, Customer, Reservation

class TestHotelMethods(unittest.TestCase):

    def setUp(self):
        """Configuración de los objetos antes de cada prueba."""
        self.hotel = Hotel(hotel_id=1, name="Hotel ABC", location="New York", rooms_available=5)
        self.customer = Customer(customer_id=1, name="John Doe", email="john.doe@example.com")

    def test_reserve_room(self):
        """Prueba para verificar que se pueda reservar una habitación."""
        self.assertTrue(self.hotel.reserve_room())  # Se debe reservar una habitación
        self.assertEqual(self.hotel.rooms_available, 4)  # Debería quedar 1 habitación menos disponible

    def test_reserve_room_no_rooms(self):
        """Prueba para verificar que no se pueda reservar si no hay habitaciones disponibles."""
        self.hotel.rooms_available = 0  # Establecemos 0 habitaciones disponibles
        self.assertFalse(self.hotel.reserve_room())  # No debería poder reservar
        self.assertEqual(self.hotel.rooms_available, 0)  # Aún debería quedar 0 habitaciones

    def test_cancel_reservation(self):
        """Prueba para verificar que se pueda cancelar una reserva y aumentar la disponibilidad."""
        self.hotel.reserve_room()  # Reservamos una habitación
        self.hotel.cancel_reservation()  # Cancelamos la reserva
        self.assertEqual(self.hotel.rooms_available, 5)  # Debería volver a estar disponible la habitación

    def test_create_reservation(self):
        """Prueba para crear una reserva y verificar los datos."""
        reservation = Reservation(reservation_id=1, customer=self.customer, hotel=self.hotel)
        self.assertEqual(reservation.reservation_id, 1)
        self.assertEqual(reservation.customer.name, self.customer.name)
        self.assertEqual(reservation.hotel.name, self.hotel.name)

    def test_reserve_multiple_rooms(self):
        """Prueba para verificar la reserva de varias habitaciones consecutivas."""
        for _ in range(5):
            self.hotel.reserve_room()
        self.assertEqual(self.hotel.rooms_available, 0)  # Después de 5 reservas, no debería haber habitaciones disponibles

    def test_create_reservation_no_rooms(self):
        """Prueba para intentar crear una reserva cuando no hay habitaciones disponibles."""
        self.hotel.rooms_available = 0  # Establecemos 0 habitaciones disponibles
        reservation = Reservation(reservation_id=2, customer=self.customer, hotel=self.hotel)
        self.assertEqual(reservation.hotel.rooms_available, 0)  # La reserva debería no afectar la disponibilidad

if __name__ == '__main__':
    unittest.main()
