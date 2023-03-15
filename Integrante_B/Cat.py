#aqui est creat la classe Cat
class Cat:
    #aqui estan definits els atributs que tenim en la classe cat
    def __init__(self, animal, alimento, edad, color):
        self.animal = animal
        self.alimento = alimento
        self.edad = edad
        self.color = color
# aqui estan los getter y los setters

    def getAnimal(self):
        return self.animal
    def setAnimal(self, animal):
        self.animal = animal

    def getAlimento(self):
        return self.alimento
    def setAlimento(self, alimento):
        self.alimento = alimento

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color


#aqui tenim la salutació per mostra per pantalla tota la classe Cat
    def salutacio(self):
        c1 = Cat()
        c1.animal = "Felino"
        c1.color = "Amarillo"
        c1.edad = "9"
        c1.alimento = "Carnívoro"
        c1.salutacio()

#Aqui tenim definida la funcio to_dict per fer la prac
    def to_dict(self):
        return {
            "Felino":self.animal,
            "Amarillo":self.color,
            "9":self.edad,
            "Carnívoro":self.alimento

        }


