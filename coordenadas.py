class Coordenada():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distancia(self, coordenada2):
        diff_x = (self.x - coordenada2.x)**2
        diff_y = (self.y - coordenada2.y)**2
        return (diff_x + diff_y)**(1/2)

if __name__ == "__main__":
    coordenada1 = Coordenada(5,10)
    coordenada2 = Coordenada(78,100)
    print(coordenada1.distancia(coordenada2))
