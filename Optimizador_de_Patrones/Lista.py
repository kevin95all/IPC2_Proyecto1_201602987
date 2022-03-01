from Nodo import Nodo


class Lista:

    def __init__(self):
        self.ini = None
        self.fin = None

    def lista_vacia(self):
        if self.ini is None:
            return True
        else:
            return False

    def agregar_ini(self, dato):
        if self.lista_vacia():  # -----> Si lista_vacia() = True entonces...
            self.ini = self.fin = Nodo(dato)  # -----> ini y fin son objetos de la clase Nodo
            self.fin.siguiente = self.ini  # -----> El apuntador de fin --> ini
        else:
            nodo_auxiliar = Nodo(dato)  # -----> nodo_auxiliar es un objeto de la clase Nodo
            nodo_auxiliar.siguiente = self.ini  # -----> El apuntador de nodo_auxiliar --> ini
            self.ini = nodo_auxiliar  # -----> El nodo_auxiliar se coloca al principio de la lista
            self.fin.siguiente = self.ini  # -----> El apuntador de fin --> ini

    def agregar_fin(self, dato):
        if self.lista_vacia():
            self.ini = self.fin = Nodo(dato)
            self.fin.siguiente = self.ini
        else:
            nodo_auxiliar = self.fin
            self.fin = nodo_auxiliar.siguiente = Nodo(dato)
            self.fin.siguiente = self.ini

    def mostrar_contenido(self):
        nodo_auxiliar = self.ini
        while nodo_auxiliar.siguiente != self.ini:
            print(nodo_auxiliar.dato)
            nodo_auxiliar = nodo_auxiliar.siguiente
        print(nodo_auxiliar.dato)
