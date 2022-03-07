class Imagen:

    def __init__(self):
        self.nombre = ''
        self.filas = 0
        self.columnas = 0
        self.patron = ''

    def generar_piso(self, nombre, filas, columnas, patron):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.patron = patron
        print('')
        print(f'N: {self.nombre}  F: {self.filas}  C: {self.columnas}  P: {self.patron}')

    def generar_patron(self):
        pass
