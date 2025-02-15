""" 
Módulo principal del sistema de reservas.
Este script maneja la creación y gestión de hoteles, clientes y reservas.
"""
from models import Hotel
from database import load_data, save_data

hotels = load_data("hotels.json")
customers = load_data("customers.json")
reservations = load_data("reservations.json")


def create_hotel():
    """ Módulo principal del sistema de reservas """
    hotel_id = input("Ingrese ID del hotel: ")
    name = input("Ingrese el nombre del hotel: ")
    location = input("Ingrese la ubicación: ")
    rooms = int(input("Ingrese número de habitaciones disponibles: "))

    hotel = Hotel(hotel_id, name, location, rooms)
    hotels.append(hotel.__dict__)
    save_data("hotels.json", hotels)
    print("Hotel creado con éxito.")
