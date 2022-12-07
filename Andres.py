class Acero():
    def __init__(self, nombre, peso, altura, ancho, espesor):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.ancho = ancho
        self.espesor = espesor

    def area(self):
        a= (self.altura+self.ancho*2)*self.espesor
        print(f"el acero tiene un area de {a} cm cuadrados")

    def anchoEfectivo(self):
        ancho = self.ancho - 4*self.espesor
        print(f"el ancho efectivo del acero ingresado es de {ancho}")    


unAcero = Acero("C20", 15.4, 20, 8, 0.25)

unAcero.area()

unAcero.anchoEfectivo()