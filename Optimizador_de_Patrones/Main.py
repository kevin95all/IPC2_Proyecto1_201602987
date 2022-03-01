from tkinter import *
from tkinter import filedialog
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
                self.cargar_archivo()

            elif self.op == '2':
                self.seleccionar_piso()

            elif self.op == '3':
                self.mostrar_piso()

            elif self.op == '4':
                self.seleccionar_patron()

            elif self.op == '5':
                self.mostrar_patron()

            elif self.op == '6':
                self.salir()

            else:
                print('                    ')
                print('--> Opción no valida')

    def cargar_archivo(self):
        ventana = Tk()
        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos XML', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        ventana.mainloop()

    def seleccionar_piso(self):
        pass

    def mostrar_piso(self):
        pass

    def seleccionar_patron(self):
        pass

    def mostrar_patron(self):
        pass

    def salir(self):
        print('                       ')
        print('--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.salida = True


app = Main()
app.menu_principal()
