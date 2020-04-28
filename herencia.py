#comprar un suscripcion
class Suscripcion:

    def __init__(self, precio_en_dolares):
        self.precio_en_dolares = precio_en_dolares 
    
    def moneda_local(self):
        return self.precio_en_dolares * 3.50
    
class SuscripcionBasic(Suscripcion):
    def __init__(self, costo):
        super().__init__(costo)

if __name__ == "__main__":
    #platzi = Suscripcion(250)
    platzi = SuscripcionBasic(85)
    print("Precio de la suscripción: {}".format(platzi.moneda_local()))