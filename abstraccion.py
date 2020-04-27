class Lavadora:

    def __init__(self):
        pass
    
    def lavar (self, temperatura='fría'):
        self._agregar_agua(temperatura)
        self._agregar_jabon()
        self._centrifugar()
        print("\n")
    
    def _agregar_agua(self,temperatura):
        print("Agregando agua {}".format(temperatura))

    def _agregar_jabon(self):
        print("Agregando Jabón!")

    def _centrifugar(self):
        print("Centrifugando!")

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
    lavadora.lavar(temperatura='caliente')