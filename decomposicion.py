class Automovil:
    def __init__(self,modelo,marca,color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(4,'gasolina')

    def acelerar (self, tipo='despacio'):
        if (tipo=='rapida'):
            print('Acelerando ...')
            self._motor.inyectar_gasolina(10)
        else:
            print('Desacelerando')
            self._motor.inyectar_gasolina(3)
        self._estado = 'en movimiento'
class Motor:

    def __init__(self,cilindros,tipo):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyectar_gasolina(self,cantidad):
        print('Cantidad de gasolina {}'.format(str(cantidad)))
        
if __name__ == "__main__":
    auto = Automovil('Renault Logan','Renault','Gris')
    auto.acelerar()
    auto.acelerar(tipo='rapida')