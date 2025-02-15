import json
import os

def load_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print(f"Error al cargar {filename}. Archivo corrupto.")
            return []

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
