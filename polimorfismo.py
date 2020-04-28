class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print("Avanzo caminando!")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print("Avanzo en un bicicleta!")

if __name__ == "__main__":
    persona = Persona("Cris")
    ciclista = Ciclista("Dani")
    persona.avanzar()
    ciclista.avanzar()