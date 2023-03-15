import json

from Integrant_A.vehicle import Vehicle
from Integrant_A.Car import Car

vehicles = [
    Vehicle("1234 ABC", "coche", "Ford", "Negro", "Bronco", "5"),
    Vehicle("2234 ABC", "coche", "Honda", "Rojo", "Navi", "5"),
    Vehicle("3234 ABC", "coche", "Hyundai", "Negro", "Klass", "5"),
    Vehicle("4234 ABC", "coche", "BMW", "Azul", "xDrive", "5"),
    Vehicle("5234 ABC", "coche", "Seat", "Negro", "ibiza", "5")

]
Cars = [
    Car("Ford", "Bronco", "Diesel", "España"),
    Car("Honda", "Navi", "Gasoil", "España"),
    Car("Hyundai", "Klass", "Diesel", "España"),
    Car("BMW", "xDrive", "Gasoil", "España"),
    Car("Seat", "ibiza", "Diesel", "España")
]

vehicles_list = [v.to_dict() for v in vehicles]
cars_list = [c.to_dict() for c in Cars]

data = {"Vehicles": vehicles_list, "Cars": cars_list}

with open("jsonAPI2/a.json", ) as file:
    json.dump(data, file)
