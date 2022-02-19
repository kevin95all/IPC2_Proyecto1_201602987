from Operaciones import Operaciones


class Main:

    def __init__(self):
        self.ruta = ''
        self.op = ''
        self.salida = False
        self.operaciones = Operaciones()

    def menu_principal(self):
        while not self.salida:
            print('                                              ')
            print('┌------------- MENU PRINCIPAL -------------┐')
            print('|                                          |')
            print('|          1)   Cargar archivo             |')
            print('|          2)   Seleccionar piso           |')
            print('|          3)   Mostrar piso               |')
            print('|          4)   Seleccionar patrón         |')
            print('|          5)   Mostrar patrón             |')
            print('|          6)   Salir                      |')
            print('|                                          |')
            print('└------------------------------------------┘')
            print('                                              ')

            self.op = input('--> Ingrese una opción: ')

            if self.op == '1':
                pass

            elif self.op == '2':
                pass

            elif self.op == '3':
                pass

            elif self.op == '4':
                pass

            elif self.op == '5':
                pass

            elif self.op == '6':
                self.salir()

            else:
                print('                    ')
                print('--> Opción no valida')

    def cargar_archivo(self):
        pass

    def salir(self):
        print('                       ')
        print('--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.salida = True


app = Main()
app.menu_principal()
