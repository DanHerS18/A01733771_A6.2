import unittest
from models import Hotel, Customer, Reservation

class TestHotel(unittest.TestCase):
    def test_reserve_room(self):
        hotel = Hotel("H001", "Hotel ABC", "Ciudad X", 5)
        self.assertTrue(hotel.reserve_room())
        self.assertEqual(hotel.rooms_available, 4)

    def test_cancel_reservation(self):
        hotel = Hotel("H002", "Hotel XYZ", "Ciudad Y", 2)
        hotel.cancel_reservation()
        self.assertEqual(hotel.rooms_available, 3)

if __name__ == '__main__':
    unittest.main()
