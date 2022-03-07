from tkinter import *
from tkinter import filedialog
from Operaciones import Operaciones


class Main:

    def __init__(self):
        self.ruta = ''
        self.op = ''
        self.salida = False
        self.piso_seleccionado = False
        self.patron_seleccionado = False
        self.operaciones = Operaciones()

    def menu_principal(self):
        while not self.salida:
            print('                                            ')
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
            print('                                            ')

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
        respaldo = self.ruta
        self.ruta = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo
            print('                              ')
            print('--> No se cargo ningun archivo')
        else:
            self.operaciones.leer_xml(self.ruta)
            print('                             ')
            print('--> Archivo cargado con exito')
        ventana.mainloop()

    def seleccionar_piso(self):
        if self.ruta == '':
            print('                                   ')
            print('--> No se ha cargado ningun archivo')
        else:
            print('                       ')
            self.operaciones.mostrar_pisos()
            self.piso_seleccionado = True

    def mostrar_piso(self):
        if self.ruta == '':
            print('                                   ')
            print('--> No se ha cargado ningun archivo')
        else:
            if not self.piso_seleccionado:
                print('                                 ')
                print('--> No se ha seleccionado un piso')
            else:
                pass

    def seleccionar_patron(self):
        if self.ruta == '':
            print('                                   ')
            print('--> No se ha cargado ningun archivo')
        else:
            if not self.piso_seleccionado:
                print('                                 ')
                print('--> No se ha seleccionado un piso')
            else:
                print('                          ')
                self.operaciones.mostrar_patrones()
                self.patron_seleccionado = True

    def mostrar_patron(self):
        if self.ruta == '':
            print('                                   ')
            print('--> No se ha cargado ningun archivo')
        else:
            if not self.piso_seleccionado:
                print('                                 ')
                print('--> No se ha seleccionado un piso')
            else:
                if not self.patron_seleccionado:
                    print('                                   ')
                    print('--> No se ha seleccionado un patron')
                else:
                    pass

    def salir(self):
        print('                       ')
        print('--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.piso_seleccionado = False
        self.patron_seleccionado = False
        self.salida = True


app = Main()
app.menu_principal()
