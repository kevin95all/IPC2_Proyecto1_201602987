from xml.dom import minidom
from Imagen import Imagen
from Lista import Lista


class Operaciones:

    def __init__(self):
        self.ruta_xml = ''
        self.pisos = Lista()
        self.m_pisos = Lista()
        self.patrones = Lista()
        self.m_patrones = Lista()
        self.imagen = Imagen()

    def leer_xml(self, ruta):
        self.ruta_xml = ruta  # -----> Obtengo la ruta del documento xml cargado
        xml = minidom.parse(self.ruta_xml)  # -----> Obtengo acceso al documento xml
        pisos = xml.getElementsByTagName('piso')  # -----> Crea una lista con los nodos de nombre "piso"

        for i in pisos:
            nombre = i.getAttribute('nombre')
            filas = i.getElementsByTagName('R')[0]
            columnas = i.getElementsByTagName('C')[0]
            voltear = i.getElementsByTagName('F')[0]
            intercambiar = i.getElementsByTagName('S')[0]
            patrones = i.getElementsByTagName('patrones')[0]

            self.m_pisos.agregar_fin(f'----------> {nombre} <----------')
            self.m_pisos.agregar_fin(f'Filas: {filas.firstChild.data.strip()}')
            self.m_pisos.agregar_fin(f'Columnas: {columnas.firstChild.data.strip()}')
            self.m_pisos.agregar_fin(f'Costo por voltear: {voltear.firstChild.data.strip()}')
            self.m_pisos.agregar_fin(f'Costo por intercambiar: {intercambiar.firstChild.data.strip()}')
            self.pisos.agregar_fin(nombre)
            self.pisos.agregar_fin(filas.firstChild.data.strip())
            self.pisos.agregar_fin(columnas.firstChild.data.strip())
            self.pisos.agregar_fin(voltear.firstChild.data.strip())
            self.pisos.agregar_fin(intercambiar.firstChild.data.strip())

            lista = patrones.getElementsByTagName('patron')
            for patron in lista:
                codigo = patron.getAttribute('codigo')

                self.m_patrones.agregar_fin(f'Codigo: {codigo}')
                self.m_patrones.agregar_fin(f'Patron: {patron.firstChild.data}')
                self.patrones.agregar_fin(codigo)
                self.patrones.agregar_fin(patron.firstChild.data)

    def mostrar_pisos(self):
        self.m_pisos.mostrar_contenido()
        print('                                ')
        nombre = input('--> Ingrese el nombre: ')
        datos = self.pisos.buscar_piso(nombre)
        patron = self.patrones.buscar_patron(datos[0])
        self.imagen.generar_piso(datos[1], datos[2], datos[3], patron)

    def mostrar_patrones(self):
        self.m_patrones.mostrar_contenido()
