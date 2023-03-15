import json

from Integrant_A.vehicle import Vehicle
from Integrant_A.Car import Car
from Integrante_B.animal import Animal
from Integrante_B.Cat import Cat

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

cats = [
    Cat("Felino", "Amarillo", "12", "Carnívor"),
    Cat("Felino", "Rojo", "6", "Carnívor"),
    Cat("Felino", "Negro", "8", "Carnívor"),
    Cat("Felino", "Blanco", "3", "Carnívor"),
    Cat("Felino", "Marron", "7", "Carnívor"),
]

animals = [
    Animal("Tigre", "Amur", "Felino", "5", "amarillo", "8-10")
    Animal("Tortuga", "Sulcata", "Bosque", "10", "verde", "50-80")
    Animal("Perro", "Boxer", "Perro, 7", "marron", "10-13")
    Animal("Tiburón", "Oceánico", "Blanco", "10", "azul", "20-30")
    Animal("Elefante", "Asiático", "Asiático", "7", "gris", "60-70")
]

cats_list = [c.to_dict() for c in cats]

animals_list = [a.to_dict() for a in animals]

data = {"Cats": cats_list, "animals":animals_list}

with open("jsonAPI2/b.jason", 'w') as file:
    json.dump(data, file)
