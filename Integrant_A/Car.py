import json
class Car:
    def __init__(self, marca, model, gasolina, pais):
        self.marca = marca
        self.model = model
        self.gasolina = gasolina
        self.pais = pais

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_gasolina(self):
        return self.gasolina

    def set_gasolina(self, gasolina):
        self.gasolina = gasolina

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais

    def salutacio(self):
        print(f"La marca és: {self.marca} "
              f"El model és: {self.model} "
              f"Gasolina: {self.gasolina} "
              f"País: {self.pais}.")
    def to_dict(self):
        return {
            "marca": self.marca,
            "model": self.model,
            "gasolina": self.gasolina,
            "pais": self.pais
        }


car = Car("Toyota", "Corolla", "Diesel", "Alemania")
car.salutacio()


