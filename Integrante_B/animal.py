class Animal:

    # aqui afegeixo els atributs que vulgui de animals
    def __int__(self, nombre, especie, tipo, edad, color, vida):
        self.nombre = nombre
        self.especie = especie
        self.tipo = tipo
        self.edad = edad
        self.color = color
        self.vida = vida


#aquest es el apratat de els get/set
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEspecie(self):
        return self.especie

    def setEspecie(self, especie):
        self.especie = especie

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo


    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getVida(self):
        return self.vida

    def setVida(self, vida):
        self.vida = vida


#aqui esta el metode a l'hora de cridar per pantalla el que vull que surti
    def salutacio(self):
        print("El nom del animal és: " + self.nombre)
        print("La seva especie  és: " + self.especie)
        print("El tipus d'animal és: " + self.tipo)
        print("L'edad que té és de  " + self.edad + "anys")
        print("El seu color principal és: " + self.color)
        print("Solen durar  " + self.vida + "anys")

    def to_dict(self):
        return {
            "Paco":self.nombre,
            "Felino":self.especie,
            "Carnívoro":self.tipo,
            "12":self.edad,
            "amarillo": self.color,
            "15": self.vida

        }